from typing import Sequence, Mapping

from dispenser_types import Dispenser, Note, Divisor, ContainerGroup
from divisor import DivisionFactory
from container_group import SingleCurrencyContainerGroup


class SingleCurrencyDispenser(Dispenser):
    def __init__(self, notes_seed: Mapping[Note, int]) -> None:
        self._containers: ContainerGroup = SingleCurrencyContainerGroup(notes_seed)
        self._divisor: Divisor = DivisionFactory(self._containers)

    def dispense(self, amount: float) -> Sequence[Note]:
        return self._containers.dispense_notes(self._divisor.subdivide(amount))
