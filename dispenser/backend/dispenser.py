from typing import Mapping

from dispenser_types import ProcessedRequest, Dispenser
from containers import NoteContainer
from notes import Note, NotePLN
from chains import ChainDivisor
from exceptions import InvalidArgumentException


class SingleCurrencyDispenser(Dispenser):
    def __init__(self, containers) -> None:

        self._processor_chain = ChainDivisor(list(containers.keys()), containers)

    def dispense(self, amount: float) -> Mapping[Note, int]:
        if amount < 0:
            raise InvalidArgumentException('Amount has to be non-negative')

        processed: ProcessedRequest = \
            self._processor_chain.process(amount)

        return self._processor_chain.handle(processed)


class BasicDispenser(SingleCurrencyDispenser):
    def __init__(self):
        super().__init__(
            {
                NotePLN(100): NoteContainer(NotePLN(100), 10**5),
                NotePLN(50): NoteContainer(NotePLN(50), 10**5),
                NotePLN(20): NoteContainer(NotePLN(20), 10**5),
                NotePLN(10): NoteContainer(NotePLN(10), 10**5)
            }
        )


basic_dispenser = BasicDispenser()
