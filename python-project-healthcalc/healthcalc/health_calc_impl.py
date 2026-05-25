import math

from healthcalc.health_calc import HealthCalc
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.gender import Gender
from healthcalc.person import Person
from healthcalc.bmi_category import BMICategory
from healthcalc.body_mass_index import BodyMassIndex


class HealthCalcImpl(HealthCalc, BodyMassIndex):

    instance = None

    @classmethod
    def getInstance(cls) -> HealthCalc:
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def bmi_classification(self, bmi: float) -> str:
        if bmi < 0:
            raise InvalidHealthDataException("BMI cannot be negative.")

        if bmi > 150:
            raise InvalidHealthDataException(
                "BMI must be within a possible biological range [0-150]."
            )

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

   

    def bmi(self, weight: float, height: float) -> float:
        if weight <= 0:
            raise InvalidHealthDataException("Weight must be positive.")

        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")

        if weight < 1 or weight > 700:
            raise InvalidHealthDataException("Weight must be within [1-700] kg.")

        if height < 0.30 or height > 3.00:
            raise InvalidHealthDataException("Height must be within [0.30-3.00] m.")

        return weight / (height ** 2)

    def bmi_person(self, person: Person) -> float:
        return self.bmi(person.weight(), person.height())

    def ibw(self, height: float, sex) -> float:
        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")

        if isinstance(sex, str):
            try:
                sex = Gender(sex)
            except ValueError:
                raise InvalidHealthDataException("Sex must be 'male' or 'female'.")

        if sex == Gender.MALE:
            return 50 + 0.9 * (height - 152.4)

        if sex == Gender.FEMALE:
            return 45.5 + 0.9 * (height - 152.4)

        raise InvalidHealthDataException("Sex must be 'male' or 'female'.")

    def ibw_person(self, person: Person) -> float:
        return self.ibw(person.height(), person.gender())

    def bmr(self, weight: float, height: float, age: int, sex) -> float:
        if weight <= 0:
            raise InvalidHealthDataException("Weight must be positive.")

        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")

        if age <= 0:
            raise InvalidHealthDataException("Age must be positive.")

        if isinstance(sex, str):
            try:
                sex = Gender(sex)
            except ValueError:
                raise InvalidHealthDataException("Sex must be 'male' or 'female'.")

        if sex == Gender.MALE:
            return (10 * weight) + (6.25 * height) - (5 * age) + 5

        if sex == Gender.FEMALE:
            return (10 * weight) + (6.25 * height) - (5 * age) - 161

        raise InvalidHealthDataException("Sex must be 'male' or 'female'.")

    def bmr_person(self, person: Person) -> float:
        return self.bmr(
            person.weight(),
            person.height(),
            person.age(),
            person.gender()
        )
    def bmi_category(self, bmi: float) -> BMICategory:
        if not isinstance(bmi, (int, float)) or not math.isfinite(bmi):
            raise InvalidHealthDataException("BMI must be a finite real number.")

        if bmi <= 0:
            raise InvalidHealthDataException("BMI must be positive.")

        if bmi > 150:
            raise InvalidHealthDataException(
                "BMI must be within a possible biological range [0-150]."
            )

        if bmi < 16.0:
            return BMICategory.SEVERE_THINNESS
        if bmi < 17.0:
            return BMICategory.MODERATE_THINNESS
        if bmi < 18.5:
            return BMICategory.MILD_THINNESS
        if bmi < 25.0:
            return BMICategory.NORMAL
        if bmi < 30.0:
            return BMICategory.OVERWEIGHT
        if bmi < 35.0:
            return BMICategory.OBESE_CLASS_I
        if bmi < 40.0:
            return BMICategory.OBESE_CLASS_II

        return BMICategory.OBESE_CLASS_III

    def category(self, person: Person) -> BMICategory:
        bmi = self.bmi_person(person)
        return self.bmi_category(bmi)

    def bmi_full_classification(self, bmi: float) -> str:
        return self.bmi_category(bmi).value
    
    def bmi_person(self, person: Person) -> float:
        return self.bmi(person.weight(), person.height())

    def body_mass_index(self, person: Person) -> float:
        return self.bmi_person(person)