import functools
import itertools
from typing import Any
from exceptions import NoteUnavailableException

import request


class ChainDivisor:
    def __init__(self, supported_notes, containers) -> None:

        self._notes = sorted(supported_notes, key=lambda note: note.value(), reverse=True)
        self._containers = containers

    def get_container(self, note):
        return self._containers.get(note)

    def _process_single_note(self, note, req):
        number_to_widthdraw = min(
            int(req.to_process() // note.value()),
            self._containers.get(note).available()
        )
        return req.order_withdrawal(note, number_to_widthdraw)

    def process(self, amount: float):
        processed = functools.reduce(
            lambda req, note_to_process:
                self._process_single_note(note_to_process, req),
            self._notes,
            request.DispenseRequest(amount)
        )
        if processed.to_process() != 0.0:
            raise NoteUnavailableException('Not enough granularity')
        else:
            return request.DispenseOutcome(processed.to_dispense())

    def handle(self, req: request.ProcessedRequest) -> Any:

        if isinstance(req, request.DispenseOutcome):
            return list(itertools.chain(*(
                self._containers.get(note).get(number)
                for note, number in req.results().items()
            )))
        else:
            return req
