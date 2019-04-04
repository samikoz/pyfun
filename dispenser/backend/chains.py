import functools
from typing import Sequence

from dispenser_types import Processor
from request import DispenseRequest


class ProcessorChain:
    def __init__(self, processors: Sequence[Processor]) -> None:

        self._processors: Sequence[Processor] = processors

    def process(self, amount: float):
        return functools.reduce(
            lambda x, processor: processor.process(x),
            self._processors,
            DispenseRequest(amount)
        )
