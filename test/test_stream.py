import operator
import pytest
import functools
import itertools

from stream import Stream


class TestStream:

    iters = (
        range(10),
        [1, -1, 1, -1, 1],
        'abcd',
    )

    @pytest.mark.parametrize('iterable', iters)
    def test_equality(self, iterable):
        assert Stream(iterable) == Stream(iterable)

    @pytest.mark.parametrize('iterable', iters)
    @pytest.mark.parametrize('unary_func', [
        lambda x: 3 * x, lambda x: (x,)
    ])
    def test_map(self, unary_func, iterable):
        assert (
            Stream(iterable).map(unary_func).to_list()
            ==
            list(map(unary_func, iterable))
        )

    @pytest.mark.parametrize('iterable', iters)
    @pytest.mark.parametrize('binary_func', [
        operator.add, lambda x, y: 2 * x + y
    ])
    def test_reduce(self, binary_func, iterable):
        assert (
            Stream(iterable).reduce(binary_func)
            ==
            functools.reduce(binary_func, iterable)
        )

    @pytest.mark.parametrize('iterable', iters)
    @pytest.mark.parametrize('afilter', [
        lambda x: x + x > x, lambda x: not x
    ])
    def test_filter(self, afilter, iterable):
        assert (
            Stream(iterable).filter(afilter).to_list()
            ==
            list(filter(afilter, iterable))
        )

    @pytest.mark.parametrize('iterable', iters)
    def test_pair_conseq(self, iterable):
        assert (
            Stream(iterable).pair_conseq().to_list()
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

    @pytest.mark.parametrize('iterable', iters)
    def test_min(self, iterable):
        assert Stream(iterable).min() == min(list(iterable))

    @pytest.mark.parametrize('iterable,condition,benchmark', [
        (range(10), lambda x: x > 5, 6),
    ])
    def test_first(self, iterable, condition, benchmark):
        assert Stream(iterable).first(condition) == benchmark
