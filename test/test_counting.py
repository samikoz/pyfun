import pytest

from fun_counting import count_bounded_integers_with_digits_from_set


class TestBoundedIntegersWithDigitsFromSet:
    digits = [0, 3, 7, 8]

    @pytest.mark.parametrize('digits,bound,length,expected_count', [
        ([2, 3, 7, 8], 8, 1, 3), ([1], 100, 2, 1), ([2, 5], 523, 3, 5)
    ])
    def test_regular_for_bound_equal_in_length(self, digits, bound, length, expected_count):
        assert count_bounded_integers_with_digits_from_set(digits, bound, length) == expected_count

    def test_bound_greater_in_length_zero_included(self):
        assert count_bounded_integers_with_digits_from_set([0, 8], 1000, 2) == 4

    def test_bound_smaller_than_length(self):
        assert count_bounded_integers_with_digits_from_set([1], 15, 3) == 0

    def test_bound_equal_to_the_only_possibility(self):
        assert count_bounded_integers_with_digits_from_set([2], 222, 3) == 0
