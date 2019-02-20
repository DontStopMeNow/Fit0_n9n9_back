from exceptions import InvalidMemorySize

from copy import deepcopy


class Memory:
    _max_memory_size = 1000

    def __init__(self, memory_size: int = 10):
        if memory_size < 1 or memory_size > self._max_memory_size:
            raise InvalidMemorySize(
                f"Memory size must be between 0 and {self._max_memory_size}")
        self._memory_size = memory_size
        self._memory = [0]*memory_size
        self._position = 0

    @property
    def memory_size(self):
        return self.memory_size

    @property
    def position(self):
        return self._position

    @property
    def memory(self):
        return deepcopy(self._memory)

    @property
    def value(self):
        return self._memory[self._position]

    def inc_position(self):
        self._position += 1
        if self.position > self._memory_size:
            self._position %= self._memory_size

    def dec_position(self):
        self._position -= 1
        if self._position < 0:
            self._position %= self._memory_size
    
    def inc_value(self):
        self._memory[self._position] += 1

    def dec_value(self):
        self._memory[self._position] -= 1
