import pytest

import sorts


class TestSorts:

    sortees_and_sorted = (
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-1, -10, 0, 5], [-10, -1, 0, 5]),
        ([1, 2, 1, -1, -1], [-1, -1, 1, 1, 2]),
    )

    @staticmethod
    def _test_sort(sorter, sortee, sorted_benchmark):
        assert sorter().sort(sortee) == sorted_benchmark

    @pytest.mark.parametrize('sorteda,sortedb,merged', [
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 4, 6], [2, 3, 5], [1, 2, 3, 4, 5, 6]),
        ([-1, 5, 10], [0, 0], [-1, 0, 0, 5, 10]),
        ([-2, ], [-3, 0, 5], [-3, -2, 0, 5]),
    ])
    def test_merge_sorted(self, sorteda, sortedb, merged):
        assert (
            sorts.MergeSorter().merge_sorted(sorteda, sortedb)
            ==
            merged
        )

    @pytest.mark.xfail
    @pytest.mark.parametrize('sorteda,sortedb,merged', [
        ([], [4, 7, 10], [4, 7, 10]),
        ([1, 2, 10], [], [1, 2, 10]),
    ])
    def test_merge_sorted_empty(self, sorteda, sortedb, merged):
        assert (
            sorts.MergeSorter().merge_sorted(sorteda, sortedb)
            ==
            merged
        )

    @pytest.mark.parametrize('sortee,sorted_benchmark', sortees_and_sorted)
    def test_mergesort(self, sortee, sorted_benchmark):
        self._test_sort(sorts.MergeSorter, sortee, sorted_benchmark)

    @pytest.mark.parametrize('sortee,sorted_benchmark', sortees_and_sorted)
    def test_bubblesort(self, sortee, sorted_benchmark):
        self._test_sort(sorts.BubbleSorter, sortee, sorted_benchmark)
