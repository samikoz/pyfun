import pytest

from fun_counting import count_bounded_integers_with_digits_from_set


class TestBoundedIntegersWithDigitsFromSet:
    digits = [0, 3, 7, 8]

    @pytest.mark.parametrize('digits,bound,length,expected_count', [
        ([0, 3, 7, 8], 8, 1, 3), ([1], 100, 2, 1), ([2, 5], 523, 2, 5)
    ])
    def test_count_bounded_integers_with_digits_from_set(self, digits, bound, length, expected_count):
        assert count_bounded_integers_with_digits_from_set(digits, bound, length) == expected_count
