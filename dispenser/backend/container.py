import itertools
from typing import Sequence
from dispenser_types import Container

from notes import Note


class NoteContainer(Container):
    def __init__(self, note: Note, seed: int) -> None:
        self._available: int = seed
        self._note: Note = note

    def available(self) -> int:
        return self._available

    def take(self, number: int) -> Sequence[Note]:
        assert self._available > number > -1

        self._available -= number
        return [self._note.clone() for _ in itertools.repeat(None, number)]


class VoidContainer(Container):
    def available(self) -> int:
        return 0

    def take(self, number: int) -> Sequence[Note]:
        return []


void_container = VoidContainer()
