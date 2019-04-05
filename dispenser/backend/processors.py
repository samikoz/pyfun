import request
from dispenser_types import Processor, Request, Container
from notes import Note
from exceptions import NoteUnavailableException


class RegularNoteProcessor(Processor):
    def __init__(self, note: Note):
        self._note = note
        self._chain = None

    def give_chain(self, chain):
        self._chain = chain

    def _notes_to_withdraw(self, amount: float) -> float:
        return min(
            int(amount // self._note.value()),
            self._check_available(self._chain.get_container(self._note))
        )

    @staticmethod
    def _check_available(container: Container) -> int:
        return container.available()

    def process(self, req: request.PendingRequest) -> \
            request.PendingRequest:

        if isinstance(req, request.DispenseRequest):
            to_widthdraw: int = self._notes_to_withdraw(
                req.to_process()
            )
            return req.order_withdrawal(self._note, to_widthdraw)
        else:
            return req


class AssertNothingRemainsProcessor(Processor):

    def give_chain(self, chain):
        pass

    def process(self, req: request.PendingRequest) -> \
            Request:

        if isinstance(req, request.DispenseRequest):
            if req.to_process() != 0.0:
                raise NoteUnavailableException('Not enough granularity')
            else:
                return request.DispenseOutcome(req.to_dispense())
        else:
            return req
