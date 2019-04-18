from typing import Mapping

from dispenser_types import Dispenser, Note, DivisorChain, ContainerChain
from divisor_chain import SingleCurrencyDivisorChain
from container_chain import SingleCurrencyContainerChain


class SingleCurrencyDispenser(Dispenser):
    def __init__(self, notes_seed: Mapping[Note, int]) -> None:
        self._container_chain: ContainerChain = SingleCurrencyContainerChain(notes_seed)
        self._divisor_chain: DivisorChain = SingleCurrencyDivisorChain(self._container_chain)

    def dispense(self, amount: float) -> Mapping[Note, int]:
        return self._container_chain.dispense_notes(self._divisor_chain.divide_into_notes(amount))
