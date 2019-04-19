import pytest

from notes import NotePLN


class TestDispenser:
    @pytest.mark.parametrize('amount,dispensed', [
        (30.0, [NotePLN(20), NotePLN(10)]),
        (90.0, [NotePLN(50), NotePLN(20), NotePLN(20), NotePLN(10)]),
        (150, [NotePLN(100), NotePLN(50)]),
        (0, [])
    ])
    def test_correct_dispense(self, unlimited_dispenser, amount, dispensed):
        assert unlimited_dispenser.dispense(amount) == dispensed

    def test_incorrect_input(self, unlimited_dispenser):
        with pytest.raises(ValueError):
            unlimited_dispenser.dispense(125.0)
