from abc import ABC, abstractmethod
from healthcalc import InvalidHealthDataException
from healthcalc.person import Person
from healthcalc.bmi_category import BMICategory


class HealthCalc(ABC):
    """Interface for the calculator of health parameters."""

    @abstractmethod
    def bmi_classification(self, bmi: float) -> str:
        """Calculate the BMI classification of a person.

        :param bmi: Body Mass Index (kg/m2)
        :return: String classification
        :raises InvalidHealthDataException: If data is out of range
        """
        pass



    @abstractmethod
    def bmi(self, weight: float, height: float) -> float:
        """Calculate the Body Mass Index (BMI).
        
        :param weight: Weight (kg)
        :param height: Height (m)
        :return: BMI value (kg/m2)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass
   
    @abstractmethod
    def ibw(self, height: float, sex: str) -> float:
        """Calculate the Ideal Body Weight (IBW).
        
        :param height: Height (cm)
        :param  sex: Sex                                        
        :return: IBW value (kg)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass
    
    @abstractmethod
    def bmr(self, weight: float, height: float, age: int, sex: str) -> float:
        """Calculate the Basal Metabolic Rate (BMR).
            
            :param weight: Weight (kg)
            :param height: Height (cm)
            :param age: Age (years)
            :param sex: Sex (male or female)
            :return: BMR value (kcal/day)
            :raises InvalidHealthDataException: If data is out of range
            """
        pass
    
    @abstractmethod
    def category(self, person: Person) -> BMICategory:
        """Return the BMI category of a person."""
        pass

    