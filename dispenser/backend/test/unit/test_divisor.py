import pytest

from dispenser_types import Divisor
from divisor import DivisionFactory


class TestDivisor:
    @pytest.mark.parametrize('amount, expected_no_of_twenties', [(120.0, 6), (290.0, 14)])
    def test_valid_subdivision(self, amount, expected_no_of_twenties, mock_container_group, mock_twenty):
        divisor: Divisor = DivisionFactory(mock_container_group)
        assert divisor.subdivide(amount).get_requested_number(mock_twenty) == expected_no_of_twenties

    def test_impossible_subdivision(self, mock_container_group):
        divisor: Divisor = DivisionFactory(mock_container_group)
        with pytest.raises(ValueError):
            divisor.subdivide(25.0)
