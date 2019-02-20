from .exceptions import InvalidStackSize, MyStackOverflow, EmptyStack

from collections import deque
from copy import deepcopy


class Stack:
    _max_size = 1000

    def __init__(self, stack_size: int = 10) -> None:
        if stack_size < 1 or stack_size > self._max_size:
            raise InvalidStackSize(
                f"Stack size must be between 0 and {self._max_size}")
        self._stack_size = stack_size
        self._stack = deque(maxlen=self._stack_size)

    @property
    def stack_size(self) -> int:
        return self._stack_size

    @property
    def stack(self) -> list:
        return list(deepcopy(self._stack))

    def push(self, value: any) -> None:
        if len(self._stack) >= self._stack_size:
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
