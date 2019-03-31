class DispenserException(Exception):
    pass


class NoteUnavailableException(DispenserException):
    pass


class InvalidArgumentException(DispenserException):
    pass
