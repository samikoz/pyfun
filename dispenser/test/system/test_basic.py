import pytest

from notes import NotePLN
from dispenser import BasicDispenser
from exceptions import NoteUnavailableException, InvalidArgumentException


class TestBasicDispenser:
    @pytest.mark.parametrize('amount,dispensed', [
        (30.0, [NotePLN(20), NotePLN(10)]),
        (80.0, [NotePLN(50), NotePLN(20), NotePLN(10)]),
        (0, [])
    ])
    def test_correct_dispense(self, amount, dispensed):
        assert BasicDispenser().dispense(amount) == dispensed

    def test_incorrect_input(self):
        with pytest.raises(NoteUnavailableException):
            BasicDispenser().dispense(125.0)

    def test_notes_unavailable(self):
        with pytest.raises(InvalidArgumentException):
            BasicDispenser().dispense(-130.0)
