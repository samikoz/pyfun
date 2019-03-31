from typing import Mapping

from dispenser_types import Container, Handler, ContainerNavigator
from chains import ProcessorChain
from notes import Note


class DispenserNavigator(ContainerNavigator):
    def __init__(self) -> None:
        self._containers: Mapping[Note, Container] = None
        self._processor_chain = None
        self._handler = None

    def point_containers(self, containers: Mapping[Note, Container]) \
            -> 'DispenserNavigator':
        self._containers: Mapping[Note, Container] = containers
        return self

    def point_processing_chain(self, proc_chain: ProcessorChain) \
            -> 'DispenserNavigator':
        self._processor_chain: ProcessorChain = proc_chain
        return self

    def point_handler(self, handl_chain: Handler) \
            -> 'DispenserNavigator':
        self._handler = handl_chain
        return self

    def request_container(self, note: Note):
        return self._containers.get(note)

    def request_processing_chain(self):
        return self._processor_chain

    def request_handler(self):
        return self._handler
