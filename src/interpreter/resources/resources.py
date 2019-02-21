from .stack import Stack
from .memory import Memory
from .output import Output


class Resources:
    def __init__(self, stack: Stack = Stack(100),
                 memory: Memory = Memory(100),
                 output: Output = Output(100)) -> None:
        self._stack = stack
        self._memory = memory
        self._output = output

    @property
    def memory(self) -> Memory:
        return self._memory

    @property
    def stack(self) -> Stack:
        return self._stack

    @property
    def output(self) -> Output:
        return self._output
