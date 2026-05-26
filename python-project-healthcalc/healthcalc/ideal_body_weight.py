from abc import ABC, abstractmethod
from .person import Person

class IdealBodyWeight(ABC):

    @abstractmethod
    def ideal_body_weight(self, person: Person) -> float:
        pass