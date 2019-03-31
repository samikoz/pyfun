from typing import MutableMapping

from notes import Note
from dispenser_types import ProcessedRequest, PendingRequest


class DispenseOutcome(ProcessedRequest):
    def __init__(self, to_dispense: MutableMapping[Note, int]) -> None:
        self._to_dispense = to_dispense

    def results(self) -> MutableMapping[Note, int]:
        return self._to_dispense


class DispenseRequest(PendingRequest):
    def __init__(self, amount: float) -> None:
        self._initial_amount: float = amount
        self._to_process: float = amount
        self._to_dispense: MutableMapping[Note, int] = {}

    def to_process(self) -> float:
        return self._to_process

    def to_dispense(self) -> MutableMapping[Note, int]:
        return self._to_dispense

    def order_withdrawal(self, note: Note, number: int) -> 'DispenseRequest':
        self._to_dispense[note] = number
        self._to_process -= number*note.value()

        return self
