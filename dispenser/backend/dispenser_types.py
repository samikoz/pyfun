# module gathering types used in the project

# the type-classes are arranged within the module with increasing generality

import abc
from typing import Sequence


class Note:
    @abc.abstractmethod
    def value(self) -> int:
        return 0

    @abc.abstractmethod
    def clone(self) -> 'Note':
        pass


class Container(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def available(self) -> int:
        return 0

    @abc.abstractmethod
    def take(self, number: int) -> Sequence[Note]:
        return []


class Division:
    @abc.abstractmethod
    def get_requested_number(self, note: Note) -> int:
        return 0


class ContainerGroup(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_available_note_types(self) -> Sequence[Note]:
        return []

    @abc.abstractmethod
    def get_available(self, note: Note) -> int:
        return 0

    @abc.abstractmethod
    def dispense_notes(self, dispense_request: Division) -> Sequence[Note]:
        return {}


class Divisor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def subdivide(self, x: float) -> Division:
        pass

    @abc.abstractmethod
    def assert_nothing_remains(self, div: Division) -> None:
        pass


class Dispenser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dispense(self, amount: float) -> Sequence[Note]:
        return []
