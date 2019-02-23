from typing import MutableSequence, AbstractSet
import pytest

from containers import NoteContainer
from notes import NotePLN
from exceptions import NoteUnavailableException


class TestNoteContainer:
    def test_legal_withdrawal(self):
        container = NoteContainer(NotePLN(20), 5)
        assert container.available() == 5

        withdrawn: MutableSequence[NotePLN] = container.get(3)
        withdrawn_types: AbstractSet[NotePLN] = set(withdrawn)

        assert len(withdrawn_types) == 1
        assert next(iter(withdrawn_types)) == NotePLN(20)
        assert container.available() == 2

    def test_illegal_withdrawal(self):
        container = NoteContainer(NotePLN(1), 2)
        with pytest.raises(NoteUnavailableException):
            container.get(3)
