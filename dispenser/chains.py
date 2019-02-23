import functools
from typing import Sequence

from dispenser_types import Processor, Container, ContainerNavigator
from request import DispenseRequest
from notes import Note


class ProcessorChain(ContainerNavigator):
    def __init__(self, processors: Sequence[Processor],
                 nav: ContainerNavigator) -> None:

        self._navigator: ContainerNavigator = nav
        self._processors: Sequence[Processor] = processors

    def navigator(self) -> ContainerNavigator:
        return self._navigator

    def request_container(self, note: Note) -> Container:
        return self.navigator().request_container(note)

    def process(self, amount: float):
        return functools.reduce(
            lambda x, processor: processor.process(x, self._navigator),
            self._processors,
            DispenseRequest(amount)
        )
