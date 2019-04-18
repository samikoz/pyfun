import itertools
from typing import Mapping, Sequence, Iterable

from container import NoteContainer, void_container
from dispenser_types import ContainerGroup, Division, Note, Container


class SingleCurrencyContainerGroup(ContainerGroup):
    def __init__(self, notes_seed: Mapping[Note, int]) -> None:
        self._available_notes: Sequence[Note] = sorted(
            notes_seed.keys(), key=lambda note: note.value(), reverse=True
        )
        self._containers: Mapping[Note, Container] = {
            note: NoteContainer(note, number)
            for note, number in notes_seed.items()
        }

    def dispense_notes(self, division: Division) -> Sequence[Note]:
        return self._wrap_into_single_sequence(
            self._take_from_container(note, division.get_requested_number(note))
            for note in self.get_available_note_types()
        )

    @staticmethod
    def _wrap_into_single_sequence(sequences: Iterable[Sequence[Note]]) -> Sequence[Note]:
        return list(itertools.chain(*sequences))

    def _take_from_container(self, note: Note, number: int) -> Sequence[Note]:
        return self._containers.get(note).take(number)

    def get_available(self, note: Note) -> int:
        return self._containers.get(note, void_container).available()

    def get_available_note_types(self) -> Sequence[Note]:
        return self._available_notes

    def _delete_from_available_types(self, note: Note) -> None:
        note_index: int = self._available_notes.index(note)
        self._available_notes = self._available_notes[:note_index] + self._available_notes[note_index+1:]
