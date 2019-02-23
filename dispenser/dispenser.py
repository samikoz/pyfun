from typing import Mapping, Sequence

from dispenser_types import Handler, Processor, ProcessedRequest, Dispenser
from processors import RegularNoteProcessor, AssertNothingRemainsProcessor
from handlers import DispenseHandler
from navigators import DispenserNavigator
from containers import NoteContainer
from notes import Note, NotePLN
from chains import ProcessorChain
from exceptions import InvalidArgumentException


class SingleCurrencyDispenser(Dispenser):
    def __init__(self, available_notes: Mapping[Note, int],
                 processors: Sequence[Processor],
                 handler: Handler) -> None:

        self._navigator: DispenserNavigator = DispenserNavigator()

        self._navigator.point_containers(
            {
                note: NoteContainer(note, available)
                for note, available in available_notes.items()
            }
        ).point_processing_chain(
            ProcessorChain(processors, self._navigator)
        ).point_handler(
            handler
        )

    def dispense(self, amount: float) -> Mapping[Note, int]:
        if amount < 0:
            raise InvalidArgumentException('Amount has to be non-negative')

        processed: ProcessedRequest = \
            self._navigator.request_processing_chain().process(amount)

        # when handler is initiated with navigator reference one won't have
        # to pass the navigator here
        return self._navigator.request_handler().handle(processed, self._navigator)


class BasicDispenser(SingleCurrencyDispenser):
    def __init__(self):
        super().__init__(
            {
                NotePLN(100): 10**5,
                NotePLN(50): 10**5,
                NotePLN(20): 10**5,
                NotePLN(10): 10**5
            },
            [
                RegularNoteProcessor(NotePLN(100)),
                RegularNoteProcessor(NotePLN(50)),
                RegularNoteProcessor(NotePLN(20)),
                RegularNoteProcessor(NotePLN(10)),
                AssertNothingRemainsProcessor()
            ],
            DispenseHandler()
        )
