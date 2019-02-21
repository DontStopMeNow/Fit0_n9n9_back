from .resources import Resources
from utils import classproperty

from copy import deepcopy
from abc import ABC, abstractmethod


class Function(ABC):
    @classproperty
    @abstractmethod
    def name() -> str:
        pass

    @classproperty
    @abstractmethod
    def args() -> list:
        pass

    @abstractmethod
    def exec(self, resources: Resources) -> None:
        pass


class FunctionsFactory:
    def __init__(self):
        self._names_to_classes = {}

        functions = Function.__subclasses__()
        for function in functions:
            self._names_to_classes[function._name] = function

    def __getitem__(self, key: str) -> Function:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        return self._names_to_classes[key]

    def keys(self) -> list:
        return self._names_to_classes.keys()


class IncPosition(Function):
    _name = ">"
    _args = []

    @classproperty
    def name(cls) -> str:
        return cls._name

    @classproperty
    def args(cls) -> str:
        return cls._args

    @staticmethod
    def exec(resources: Resources) -> None:
        resources.memory.inc_position()


class DecPosition(Function):
    _name = "<"
    _args = []

    @classproperty
    def name(cls) -> str:
        return cls._name

    @classproperty
    def args(cls) -> str:
        return cls._args

    @staticmethod
    def exec(resources: Resources) -> None:
        resources.memory.dec_position()


class IncValue(Function):
    _name = "+"
    _args = []

    @classproperty
    def name(cls) -> str:
        return cls._name

    @classproperty
    def args(cls) -> str:
        return cls._args

    @staticmethod
    def exec(resources: Resources) -> None:
        resources.memory.inc_value()


class DecValue(Function):
    _name = "-"
    _args = []

    @classproperty
    def name(cls) -> str:
        return cls._name

    @classproperty
    def args(cls) -> str:
        return cls._args

    @staticmethod
    def exec(resources: Resources) -> None:
        resources.memory.dec_value()


class PutChar(Function):
    _name = "."
    _args = []

    @classproperty
    def name(cls) -> str:
        return cls._name

    @classproperty
    def args(cls) -> str:
        return cls._args

    @staticmethod
    def exec(resources: Resources) -> None:
        value = chr(resources.memory.value)
        resources.output.print_ch(value)

