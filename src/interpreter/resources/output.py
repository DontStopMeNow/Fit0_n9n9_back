from .exceptions import InvalidOutputSize, OutputOverflow

from copy import deepcopy


class Output:
    _max_size = 1000

    def __init__(self, size: int = 100) -> None:
        if size < 0 or size > self._max_size:
            raise InvalidOutputSize(
                f"Output size must be between 0 and {self._max_size}")
        self._size = size
        self._output = []

    @property
    def size(self) -> int:
        return self._size

    @property
    def output(self) -> list:
        return deepcopy(self._output)

    def print_ch(self, char: str) -> None:
        if len(char) != 1:
            raise TypeError("Output class can print only one character")
        if len(self._output) < self._size:
            self._output.append(char)
        else:
            raise OutputOverflow("Output overflow")
