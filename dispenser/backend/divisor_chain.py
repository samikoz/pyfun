import functools
import itertools
from typing import Any, MutableMapping

from dispenser_types import Note, Chain, ContainerChain, DividedRequest


class SingleCurrencyDispenseRequest(DividedRequest):
    def __init__(self, amount: float) -> None:
        self._initial_amount: float = amount
        self._amount_left: float = amount
        self._to_dispense: MutableMapping[Note, int] = {}

    def get_amount_to_process(self) -> float:
        return self._amount_left

    def assert_nothing_remains(self):
        if self._amount_left:
            raise ValueError(
                'Cannot realise dispense request with available notes'
            )
        return self

    def order_withdrawal(self, note: Note, number: int) -> 'SingleCurrencyDispenseRequest':
        self._to_dispense[note] = number
        self._amount_left -= number * note.value()

        return self


class SingleCurrencyDivisorChain(Chain):
    def __init__(self, container_chain: ContainerChain) -> None:
        self._containers: ContainerChain = container_chain

    def _process_single_note(self, note: Note, req: SingleCurrencyDispenseRequest) -> SingleCurrencyDispenseRequest:
        number_to_withdraw: int = min(
            int(req.get_amount_to_process() // note.value()),
            self._containers.get_available_amount(note)
        )
        return req.order_withdrawal(note, number_to_withdraw)

    def process(self, amount: float) -> DividedRequest:
        processed: SingleCurrencyDispenseRequest = functools.reduce(
            lambda req, note_to_process:
                self._process_single_note(note_to_process, req),
            self._containers.get_available_notes(),
            SingleCurrencyDispenseRequest(amount)
        )
        return processed.assert_nothing_remains()
