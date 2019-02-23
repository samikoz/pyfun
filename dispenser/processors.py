import request
from dispenser_types import Processor, Request, Container, Navigator
from dispenser_types import ContainerNavigator
from notes import Note
from exceptions import NoteUnavailableException


class RegularNoteProcessor(Processor):
    def __init__(self, note: Note):
        self._note = note

    def _notes_to_withdraw(self, amount: float, container: Container) -> float:
        return min(
            int(amount // self._note.value()),
            self._check_available(container)
        )

    @staticmethod
    def _check_available(container: Container) -> int:
        return container.available()

    def _request_container(self, navigator: ContainerNavigator) -> Container:
        return navigator.request_container(self._note)

    def process(self, req: request.PendingRequest, nav: ContainerNavigator) -> \
            request.PendingRequest:

        if isinstance(req, request.DispenseRequest):
            to_widthdraw: int = self._notes_to_withdraw(
                req.to_process(),
                self._request_container(nav)
            )
            return req.order_withdrawal(self._note, to_widthdraw)
        else:
            return req


class AssertNothingRemainsProcessor(Processor):

    def process(self, req: request.PendingRequest, nav: Navigator=None) -> \
            Request:

        if isinstance(req, request.DispenseRequest):
            if req.to_process() != 0.0:
                raise NoteUnavailableException('Not enough granularity')
            else:
                return request.DispenseOutcome(req.to_dispense())
        else:
            return req
