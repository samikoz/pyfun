from request import DispenseRequest, PendingRequest
from chains import ChainDivisor
from navigators import DispenserNavigator
from notes import NotePLN
from containers import NoteContainer
import processors


class TestRegularProcessing:
    def test_processing(self):
        req: PendingRequest = DispenseRequest(24.0)
        proc: processors.Processor = processors.RegularNoteProcessor(NotePLN(5))
        nav: DispenserNavigator = DispenserNavigator()
        nav.point_containers({NotePLN(5): NoteContainer(NotePLN(5), 3)})
        chain: ChainDivisor = ChainDivisor([proc], nav)

        processed: PendingRequest = proc.process(req, chain)

        assert processed.to_process() == 9.0
        assert processed.to_dispense().get(NotePLN(5)) == 3
