class FunctionAlreadyExist(RuntimeError):
    pass


class InvalidProgramm(RuntimeError):
    pass


class InvalidBrackets(InvalidProgramm):
    pass


class InvalidToken(InvalidProgramm):
    pass