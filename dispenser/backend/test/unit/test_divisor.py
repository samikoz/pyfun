import pytest


class TestDivisor:
    @pytest.mark.parametrize('amount, no_of_twenties', [(120.0, 1), (290.0, 2)])
    def test_valid_subdivision(self, amount, no_of_twenties):
        pass

    def test_impossible_subdivision(self):
        pass
