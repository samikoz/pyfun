from dispenser_types import Note


class NotePLN(Note):
    def __init__(self, value: int) -> None:
        super().__init__(value, 'PLN')
