import itertools
from typing import Any

from dispenser_types import Handler
import request


class DispenseHandler(Handler):
    def give_containers(self, containers):
        self._containers = containers

    def handle(self, req: request.ProcessedRequest) -> Any:

        if isinstance(req, request.DispenseOutcome):
            return list(itertools.chain(*(
                self._containers.get(note).get(number)
                for note, number in req.results().items()
            )))
        else:
            return req
