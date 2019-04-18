import itertools
from typing import MutableSequence
from dispenser_types import Container

from notes import Note


class NoteContainer(Container):
    def __init__(self, note: Note, seed: int) -> None:
        self._available: int = seed
        self._note: Note = note

    def available(self) -> int:
        return self._available

    def get(self, number: int) -> MutableSequence[Note]:
        assert self._available > number

        self._available -= number
        return [self._note.clone() for _ in itertools.repeat(None, number)]


class VoidContainer(Container):
    def available(self) -> int:
        return 0

    def get(self, number: int) -> MutableSequence[Note]:
        return []


void_container = VoidContainer()
