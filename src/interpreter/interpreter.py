from .resources import Resources
from .functions import FunctionsFactory
from .exceptions import InvalidBrackets, InvalidToken, InvalidProgramm

from collections import deque


class Interpreter:
    _spesial_symbols = set(["[", "]"])
    _start_token = "ну_девчата"
    _end_token = "дошумелись"
    _functions = FunctionsFactory()

    def __init__(self, resources: Resources) -> None:
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
                    raise InvalidBrackets("Too much closing of cycle")
                last = d.pop()
                d[-1].append(last)
            else:
                t = self._parse(token)
                if t is not None:
                    d[-1].append(t)
        if brackets_counter > 0:
            raise InvalidBrackets("Cycle not closed")
        if len(d) != 1:
            raise InvalidProgramm("Blocks parsing error")
        return d[0]

    def _parse(self, token: str) -> any:
        f_names = self._functions.keys()

        if token in f_names:
            return token
        elif token.isdigit():
            return int(token)
        elif token == self._start_token or token == self._end_token:
            return None
        else:
            raise InvalidToken(f"Invalid token \"{token}\"")

    def execute(self) -> dict:
        return self._execute_block(self._programm)

    def _execute_block(self, tokens: list) -> dict:
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if isinstance(token, list):
                while self._resources.memory.value > 0:
                    self._execute_block(token)
            elif isinstance(token, str):
                func = self._functions[token]
                args_types = func.args
                args = []

                for arg_type in args_types:
                    i += 1
                    if i == len(tokens):
                        raise TypeError("No argument")
                    arg = tokens[i]
                    if not isinstance(arg, arg_type):
                        raise TypeError("Invalid function argument type")
                    args.append(arg)
                
                func.exec(self._resources, *args)
            else:
                raise InvalidProgramm(f"Invalid token \"{token}\"")
            i += 1
        return {
            "result": "ok",
            "memory": self._resources.memory.memory,
            "output": self._resources.output.output,
            "stack": self._resources.stack.stack,
        }

