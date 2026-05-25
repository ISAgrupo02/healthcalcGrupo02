from abc import ABC, abstractmethod
from healthcalc.person import Person


class OtraMetrica(ABC):

    @abstractmethod
    def m(self, person: Person) -> float:
        pass