from typing import MutableSequence

import pytest

import processors
from dispenser_types import Container
from notes import NotePLN, Note
from exceptions import NoteUnavailableException
from request import PendingRequest, DividedRequest, DispenseRequest
from navigators import ContainerNavigator


class MockRequest(DispenseRequest):
    def __init__(self, amount):
        self._to_process = amount
        self._to_dispense = {}

    def to_process(self):
        return self._to_process

    def to_dispense(self):
        return self._to_dispense

    def order_withdrawal(self, note, number):
        self._to_dispense[note] = number
        self._to_process -= number*note.value()


class MockContainer(Container):
    def __init__(self, mock_available):
        self._mock_available = mock_available

    def get(self, number: int) -> MutableSequence[Note]:
        pass

    def available(self):
        return self._mock_available


class MockNavigator(ContainerNavigator):
    def __init__(self, mock_container):
        self._container = mock_container

    def request_container(self, note):
        return self._container


class TestRegularNoteProcessor:
    def test_notes_to_withdraw(self):
        amount = 22
        container: Container = MockContainer(2)
        proc = processors.RegularNoteProcessor(NotePLN(5))

        assert 2 == proc._notes_to_withdraw(
            amount,
            container
        )


class TestAssertNothingToProcessProcessor:
    def test_nothing_left_to_process(self):
        req: PendingRequest = MockRequest(0.0)

        proc: processors = processors.AssertNothingRemainsProcessor()
        assert isinstance(proc.process(req), DividedRequest)

    def test_not_fully_processed(self):
        req: PendingRequest = MockRequest(12.0)

        proc: processors = processors.AssertNothingRemainsProcessor()
        with pytest.raises(NoteUnavailableException):
            proc.process(req)
