from typing import Mapping, Sequence

from dispenser_types import Dispenser, Note, ChainDivisor
from chains import SingleCurrencyChainDivisor


class SingleCurrencyDispenser(Dispenser):
    def __init__(self, notes_seed: Mapping[Note, int]) -> None:
        self._available_notes: Sequence[Note] = sorted(
            notes_seed.keys(), key=lambda note: note.value(), reverse=True
        )
        self._chain: ChainDivisor = SingleCurrencyChainDivisor(notes_seed)

    def dispense(self, amount: float) -> Mapping[Note, int]:
        return self._chain.handle(self._chain.process(amount))
