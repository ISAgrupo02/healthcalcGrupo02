from abc import ABC, abstractmethod
from .gender import Gender


class Person(ABC):

    @abstractmethod
    def weight(self) -> float:
        pass

    @abstractmethod
    def height(self) -> float:
        pass

    @abstractmethod
    def gender(self) -> Gender:
        pass

    @abstractmethod
    def age(self) -> int:
        pass