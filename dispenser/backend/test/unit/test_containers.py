from typing import Sequence

from container import CloningContainer
from container_group import SingleCurrencyContainerGroup
from dispenser_types import Container, Note, ContainerGroup


class TestSingleCloningContainer:
    def test_reducing_available(self, mock_twenty):
        container: Container = CloningContainer(mock_twenty, 10)
        taken: Sequence[Note] = container.take(7)
        assert len(taken) == 7
        assert container.available() == 3


class TestSingleCurrencyContainerGroup:
    def test_dispensing(self, mock_always_two_division, mock_twenty, mock_tener):
        containers: ContainerGroup = SingleCurrencyContainerGroup({
            mock_tener: 5,
            mock_twenty: 15
        })
        dispensed: Sequence[Note] = containers.dispense_notes(mock_always_two_division)
        values: Sequence[int] = [note.value() for note in dispensed]
        assert values == [20, 20, 10, 10]
