import functools
from typing import Any


from dispenser_types import Note


@functools.total_ordering
class OrderableNote(Note):
    def __init__(self, value: int, currency: str = '') -> None:
        self._value: int = value
        self._currency: str = currency

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, OrderableNote) and self._currency == other._currency and self.value() == other.value()

    def __hash__(self) -> int:
        return hash(self.value())

    def __repr__(self) -> str:
        return f'Note({self.value()}{self._currency})'

    def __lt__(self, other: Any):
        if not isinstance(other, OrderableNote) or self._currency != other._currency:
            raise ValueError('Can only compare notes of the same currency')
        return self.value() < other.value()

    def value(self) -> int:
        return self._value

    def clone(self) -> 'Note':
        return OrderableNote(self.value(), self._currency)


class NotePLN(OrderableNote):
    def __init__(self, value: int) -> None:
        super().__init__(value, 'PLN')
