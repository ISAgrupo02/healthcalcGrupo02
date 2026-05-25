from abc import ABC, abstractmethod

from healthcalc.person import Person
from healthcalc.bmi_category import BMICategory


class BodyMassIndex(ABC):

    @abstractmethod
    def body_mass_index(self, person: Person) -> float:
        pass

    @abstractmethod
    def category(self, person: Person) -> BMICategory:
        pass