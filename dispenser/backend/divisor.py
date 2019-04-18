from typing import MutableMapping

from dispenser_types import Note, Divisor, ContainerGroup, Division


class SubdividedAmount(Division):
    def __init__(self, amount: float, containers: ContainerGroup) -> None:
        self._amount_left: float = amount
        self._to_dispense: MutableMapping[Note, int] = {}
        self._containers: ContainerGroup = containers

    def subdivide(self) -> Division:
        for note in self._containers.get_available_note_types():
            self._divide_by_note(note)

        self._assert_nothing_remains()
        return self

    def _divide_by_note(self, note: Note) -> None:
        number_to_withdraw: int = min(
            int(self._amount_left // note.value()),
            self._containers.get_available(note)
        )
        self._save_single_withdrawal_request(note, number_to_withdraw)

    def _save_single_withdrawal_request(self, note: Note, number: int) -> None:
        self._to_dispense[note] = number
        self._amount_left -= number * note.value()

    def _assert_nothing_remains(self) -> None:
        if self._amount_left:
            raise ValueError('Cannot realise dispense request with available notes')

    def get_requested_number(self, note: Note) -> int:
        return self._to_dispense.get(note, 0)


class DivisionFactory(Divisor):
    def __init__(self, container_chain: ContainerGroup) -> None:
        self._containers: ContainerGroup = container_chain

    def subdivide(self, amount: float) -> Division:
        return SubdividedAmount(amount, self._containers).subdivide()
