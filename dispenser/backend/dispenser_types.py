import abc
import functools
from typing import Any, MutableSequence, Mapping, Sequence


@functools.total_ordering
class Note:
    def __init__(self, value: int, currency: str = '') -> None:
        self._value: int = value
        self._currency: str = currency

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, Note)
            and
            self._currency == other._currency
            and
            self.value() == other.value()
        )

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


class DividedRequest:
    @abc.abstractmethod
    def get_requested_number(self, note: Note) -> int:
        return 0

    @abc.abstractmethod
    def assert_nothing_remains(self):
        pass


class Dispenser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dispense(self, amount: float) -> Mapping[Note, int]:
        return {}


class DivisorChain(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def divide_into_notes(self, x: float) -> DividedRequest:
        pass


class ContainerChain(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_available_notes(self) -> Sequence[Note]:
        return []

    @abc.abstractmethod
    def get_available_amount(self, note: Note) -> int:
        return 0

    @abc.abstractmethod
    def dispense_notes(self, dispense_request: DividedRequest) -> Mapping[Note, int]:
        return {}


class Container(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def available(self) -> int:
        return 0

    @abc.abstractmethod
    def get(self, number: int) -> MutableSequence[Note]:
        return []
