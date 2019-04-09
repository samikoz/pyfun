import functools
import itertools
from typing import Any, Mapping, Sequence
from exceptions import NoteUnavailableException

from containers import NoteContainer
from dispenser_types import Note, ChainDivisor, Container
import request


class SingleCurrencyChainDivisor(ChainDivisor):
    def __init__(self, notes_seed: Mapping[Note, int]) -> None:
        self._notes: Sequence[Note] = sorted(
            notes_seed, key=lambda note: note.value(), reverse=True
        )
        self._containers: Mapping[Note, Container] = {
            note: NoteContainer(note, number)
            for note, number in notes_seed.items()
        }

    def _process_single_note(self, note: Note, req: request.PendingRequest) -> request.PendingRequest:
        number_to_widthdraw: int = min(
            int(req.to_process() // note.value()),
            self._containers.get(note).available()
        )
        return req.order_withdrawal(note, number_to_widthdraw)

    def process(self, amount: float) -> request.DispenseOutcome:
        processed: request.PendingRequest = functools.reduce(
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
