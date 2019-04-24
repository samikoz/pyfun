import pytest
import itertools
from typing import Sequence

from notes import NotePLN
from dispenser_types import ContainerGroup, Note, Division
from dispenser import SingleCurrencyDispenser


class MockTwenty(Note):
    def value(self) -> int:
        return 20

    def clone(self) -> 'Note':
        return MockTwenty()


class MockSingleTwentyContainer(ContainerGroup):
    def get_available_note_types(self) -> Sequence[Note]:
        return [MockTwenty()]

    def get_available(self, note: Note) -> int:
        assert isinstance(note, MockTwenty)
        return 10**5

    def dispense_notes(self, dispense_request: Division) -> Sequence[Note]:
        return [MockTwenty() for _ in itertools.repeat(None, dispense_request.get_requested_number(MockTwenty()))]


@pytest.fixture()
def unlimited_dispenser():
    return SingleCurrencyDispenser({
        NotePLN(10): 10**5,
        NotePLN(20): 10**5,
        NotePLN(50): 10**5,
        NotePLN(100): 10**5
    })


@pytest.fixture()
def mock_twenty():
    return MockTwenty()


@pytest.fixture()
def mock_container_group():
    return MockSingleTwentyContainer()
