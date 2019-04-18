# module gathering types used in the project

# the type-classes are arranged within the module with increasing generality

import abc
import functools
from typing import Any, Sequence


@functools.total_ordering
class Note:
    def __init__(self, value: int, currency: str = '') -> None:
        self._value: int = value
        self._currency: str = currency

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Note) and self._currency == other._currency and self.value() == other.value()

    def __hash__(self) -> int:
        return hash(self.value())

    def __repr__(self) -> str:
        return f'Note({self.value()}{self._currency})'

    def __lt__(self, other: Any):
        if not isinstance(other, Note) or self._currency != other._currency:
            raise ValueError('Can only compare notes of the same currency')
        return self.value() < other.value()

    def value(self) -> int:
        return self._value

    def clone(self) -> 'Note':
        return Note(self.value(), self._currency)


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


class Dispenser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dispense(self, amount: float) -> Sequence[Note]:
        return []
