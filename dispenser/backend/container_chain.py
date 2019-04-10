import itertools
from typing import Mapping, Sequence

from containers import NoteContainer, void_container
from dispenser_types import ContainerChain, DividedRequest, Note, Container


class SingleCurrencyContainerChain(ContainerChain):
    def __init__(self, notes_seed: Mapping[Note, int]) -> None:
        self._available_notes: Sequence[Note] = sorted(
            notes_seed.keys(), key=lambda note: note.value(), reverse=True
        )
        self._containers: Mapping[Note, Container] = {
            note: NoteContainer(note, number)
            for note, number in notes_seed.items()
        }

    def get_available_notes(self) -> Sequence[Note]:
        return self._available_notes

    def get_available_amount(self, note: Note) -> int:
        return self._containers.get(note, void_container).available()

    def _delete_from_available(self, note: Note) -> None:
        note_index: int = self._available_notes.index(note)
        self._available_notes = self._available_notes[:note_index] + \
            self._available_notes[note_index+1:]

    def process(self, req: DividedRequest) -> Sequence[Note]:
        req.assert_nothing_remains()
        return list(itertools.chain(*(
            self._containers.get(note).get(req.get_requested_number(note)) for note in self.get_available_notes()
        )))
