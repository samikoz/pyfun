import abc
import functools
from typing import MutableMapping, Any, MutableSequence, Mapping


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


class Request(metaclass=abc.ABCMeta):
    pass


class PendingRequest(Request):
    @abc.abstractmethod
    def to_process(self) -> float:
        return 0

    @abc.abstractmethod
    def to_dispense(self) -> MutableMapping[Note, int]:
        return {}

    @abc.abstractmethod
    def order_withdrawal(self, note: Note, number: int) -> 'PendingRequest':
        pass


class ProcessedRequest(Request):
    @abc.abstractmethod
    def results(self) -> Any:
        pass


class Dispenser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dispense(self, amount: float) -> Mapping[Note, int]:
        return {}


class ChainDivisor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def process(self, amount: float) -> ProcessedRequest:
        pass

    @abc.abstractmethod
    def handle(self, request: ProcessedRequest) -> Any:
        pass


class Container(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def available(self) -> int:
        return 0

    @abc.abstractmethod
    def get(self, number: int) -> MutableSequence[Note]:
        return []
