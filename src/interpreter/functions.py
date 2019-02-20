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
