from .resources import Resources
from .functions import FunctionsFactory
from .exceptions import InvalidBrackets, InvalidToken, InvalidProgramm

from collections import deque


class Interpreter:
    _spesial_symbols = set(["[", "]"])
    _start_token = "start"
    _end_token = "end"
    _functions = FunctionsFactory()

    def __init__(self, resources: Resources = Resources()) -> None:
        self._resources = resources
        self._sources = None
        self._tokens = None
        self._programm = None

    @property
    def resources(self) -> Resources:
        return self._resources

    @property
    def programm(self) -> str:
        return self._programm

    @programm.setter
    def programm(self, value: str) -> None:
        self._sources = value
        self._tokens = self._tokenize(value)
        self._programm = self._parse_blocks(self._tokens)

    def _tokenize(self, programm: str) -> list:
        return programm.split()

    def _parse_blocks(self, tokens: list) -> list:
        if tokens[0] != self._start_token:
            raise InvalidProgramm(
                f"Programm must start with \"{self._start_token}\"")
        if tokens[-1] != self._end_token:
            raise InvalidProgramm(
                f"Programm must ends with \"{self._end_token}\"")

        d = deque()
        d.append([])
        brackets_counter = 0

        for token in tokens:
            if token == "[":
                d.append([])
                brackets_counter += 1
            elif token == "]":
                brackets_counter -= 1
                if brackets_counter < 0:
                    InvalidBrackets("Too much closing of cycle")
                last = d.pop()
                d[-1].append(last)
            else:
                t = self._parse(token)
                if t is not None:
                    d[-1].append(t)
        if brackets_counter > 0:
            raise InvalidBrackets("Cycle not closed")
        if len(d) != 1:
            raise RuntimeError("Blocks parsing error")
        return d[0]

    def _parse(self, token: str) -> any:
        f_names = self._functions.keys()

        if token in f_names:
            return self._functions[token]
        elif token.isdigit():
            return int(token)
        elif token == self._start_token or token == self._end_token:
            return None
        else:
            raise InvalidToken(f"Invalid token \"{token}\"")
