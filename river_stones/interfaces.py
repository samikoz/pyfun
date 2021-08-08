from __future__ import annotations

import abc


class ConnectableInterface:
    @abc.abstractmethod
    def is_connected(self, other: ConnectableInterface) -> bool:
        pass
