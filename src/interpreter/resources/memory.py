from .exceptions import InvalidMemorySize

from copy import deepcopy


class Memory:
    _max_size = 1000

    def __init__(self, size: int = 10) -> None:
        if size < 1 or size > self._max_size:
            raise InvalidMemorySize(
                f"Memory size must be between 0 and {self._max_size}")
        self._size = size
        self._memory = [0]*size
        self._position = 0

    @property
    def size(self) -> int:
        return self._size

    @property
    def position(self) -> int:
        return self._position

    @property
    def memory(self) -> list:
        return deepcopy(self._memory)

    @property
    def value(self) -> int:
        return self._memory[self._position]

    @value.setter
    def value(self, value: int) -> None:
        self._memory[self._position] = value

    def inc_position(self) -> None:
        self._position += 1
        if self.position > self._size:
            self._position %= self._size

    def dec_position(self) -> None:
        self._position -= 1
        if self._position < 0:
            self._position %= self._size

    def inc_value(self) -> None:
        self._memory[self._position] += 1

    def dec_value(self) -> None:
        self._memory[self._position] -= 1
