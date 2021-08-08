from __future__ import annotations

from typing import Generic, TypeVar, List, Set as SetType, Iterable, Iterator, AbstractSet
from collections.abc import Set

from river_stones.interfaces import ConnectableInterface

C = TypeVar('C', bound=ConnectableInterface)


class ConnectedComponent(Generic[C], Set):
    def __init__(self, initial_member: C) -> None:
        self.component: SetType[C] = {initial_member}

    def add(self, elements: SetType[C]) -> None:
        component_elements: List[C] = list(self.component)
        component_index: int = 0
        while component_index < len(component_elements):
            connected: List[C] = self._get_all_connected(component_elements[component_index], elements)
            component_elements.extend(connected)
            elements = set(elements).difference(connected)
            component_index += 1

        self.component = set(component_elements)

    @staticmethod
    def _get_all_connected(connectee: C, candidates: Iterable[C]) -> List[C]:
        return list(filter(lambda x: connectee.is_connected(x), candidates))

    def __iter__(self) -> Iterator[C]:
        return iter(self.component)

    def __len__(self) -> int:
        return len(self.component)

    def __contains__(self, x: object) -> bool:
        return object in self.component

    def intersection(self, s: AbstractSet[C]) -> AbstractSet:
        return self.component.intersection(s)

    def union(self, s: AbstractSet[C]) -> AbstractSet[C]:
        return self.component.union(s)

    def difference(self, s: AbstractSet[C]) -> AbstractSet[C]:
        return self.component.difference(s)
