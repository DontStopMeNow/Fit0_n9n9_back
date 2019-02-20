from .stack import Stack
from .memory import Memory


class Resources:
    def __init__(self, stack: Stack = Stack(100), memory: Memory = Memory(100)) -> None:
        self._memory = memory
        self._stack = stack

    @property
    def memory(self) -> Memory:
        return self._memory

    @property
    def stack(self) -> Stack:
        return self._stack
