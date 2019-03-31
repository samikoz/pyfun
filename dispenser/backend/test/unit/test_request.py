from notes import NotePLN
from dispenser_types import PendingRequest
from request import DispenseRequest


class TestDispenseRequest:
    def test_deduct(self):
        req: PendingRequest = DispenseRequest(150.0)
        assert req.to_process() == 150.0

        req.order_withdrawal(NotePLN(20), 2)
        assert req.to_process() == 110.0
        assert req.to_dispense().get(NotePLN(20)) == 2
