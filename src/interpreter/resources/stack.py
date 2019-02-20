from exceptions import InvalidStackSize, MyStackOverflow, EmptyStack

from collections import deque
from copy import deepcopy


class Stack:
    _max_size = 1000

    def __init__(self, size: int = 10) -> None:
        if size < 1 or size > self._max_size:
            raise InvalidStackSize(
                f"Stack size must be between 0 and {self._max_size}")
        self._size = size
        self._stack = deque(maxlen=size)

    @property
    def size(self) -> int:
        return self._size

    @property
    def stack(self) -> list:
        return list(deepcopy(self._stack))

    def push(self, value: any) -> None:
        if len(self._stack) >= self._size:
            raise MyStackOverflow("Stack overflow")
        self._stack.append(value)

    def pop(self) -> any:
        if len(self._stack < 1):
            raise EmptyStack("Stack is empty")
        return self._stack.pop()

    def peek(self) -> any:
        if len(self._stack < 1):
            raise EmptyStack("Stack is empty")
        return self._stack[-1]
