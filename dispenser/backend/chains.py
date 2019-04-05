import functools
import itertools
from typing import Sequence, Any

from dispenser_types import Processor
import request


class ProcessorChain:
    def __init__(self, processors: Sequence[Processor], containers) -> None:

        self._processors: Sequence[Processor] = processors
        for processor in self._processors:
            processor.give_chain(self)

        self._containers = containers

    def get_container(self, note):
        return self._containers.get(note)

    def process(self, amount: float):
        return functools.reduce(
            lambda x, processor: processor.process(x),
            self._processors,
            request.DispenseRequest(amount)
        )

    def handle(self, req: request.ProcessedRequest) -> Any:

        if isinstance(req, request.DispenseOutcome):
            return list(itertools.chain(*(
                self._containers.get(note).get(number)
                for note, number in req.results().items()
            )))
        else:
            return req
