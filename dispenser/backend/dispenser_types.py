import abc
from typing import MutableMapping, Any, MutableSequence, Mapping

from notes import Note


class Dispenser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dispense(self, amount: float) -> Mapping[Note, int]:
        return {}


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


class Container(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def available(self) -> int:
        return 0

    @abc.abstractmethod
    def get(self, number: int) -> MutableSequence[Note]:
        return []
