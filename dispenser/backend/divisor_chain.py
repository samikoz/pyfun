import functools
from typing import MutableMapping

from dispenser_types import Note, DivisorChain, ContainerChain, DividedRequest


class SingleCurrencyDispenseRequest(DividedRequest):
    def __init__(self, amount: float) -> None:
        self._initial_amount: float = amount
        self._amount_left: float = amount
        self._to_dispense: MutableMapping[Note, int] = {}

    def get_amount_to_process(self) -> float:
        return self._amount_left

    def get_requested_number(self, note: Note) -> int:
        return self._to_dispense.get(note, 0)

    def assert_nothing_remains(self):
        if self._amount_left:
            raise ValueError('Cannot realise dispense request with available notes')
        return self

    def order_withdrawal(self, note: Note, number: int) -> 'SingleCurrencyDispenseRequest':
        self._to_dispense[note] = number
        self._amount_left -= number * note.value()

        return self


class SingleCurrencyDivisorChain(DivisorChain):
    def __init__(self, container_chain: ContainerChain) -> None:
        self._containers: ContainerChain = container_chain

    def _process_single_note(self, note: Note, req: SingleCurrencyDispenseRequest) -> SingleCurrencyDispenseRequest:
        # think whether cannot reduce signature in easily understandable way
        number_to_withdraw: int = min(
            int(req.get_amount_to_process() // note.value()),
            self._containers.get_available_amount(note)
        )
        return req.order_withdrawal(note, number_to_withdraw)

    def divide_into_notes(self, amount: float) -> DividedRequest:
        return functools.reduce(
            lambda req, note_to_process: self._process_single_note(note_to_process, req),
            self._containers.get_available_notes(),
            SingleCurrencyDispenseRequest(amount)
        )
