import itertools
from typing import Any

from dispenser_types import Handler
import request
from navigators import DispenserNavigator


class DispenseHandler(Handler):
    def handle(self, req: request.ProcessedRequest, nav: DispenserNavigator) \
            -> Any:

        if isinstance(req, request.DispenseOutcome):
            return list(itertools.chain(*(
                nav.request_container(note).get(number)
                for note, number in req.results().items()
            )))
        else:
            return req
