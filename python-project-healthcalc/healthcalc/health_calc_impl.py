import math
from healthcalc.health_calc import HealthCalc
from healthcalc.exceptions import InvalidHealthDataException


class HealthCalcImpl(HealthCalc):

    #BMI CLASSIFICATION BASIC

    def bmi_classification(self, bmi: float) -> str:

        if bmi < 0:
            raise InvalidHealthDataException("BMI cannot be negative.")

        if bmi > 150:
            raise InvalidHealthDataException("BMI must be within a possible biological range [0-150].")

        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Normal weight"

        elif bmi < 30:
            return "Overweight"

        else:
            return "Obesity"


    #BMI FULL CLASSIFICATION

    def bmi_full_classification(self, bmi: float) -> str:

        if not isinstance(bmi, (int, float)) or not math.isfinite(bmi):
            raise InvalidHealthDataException("BMI must be a finite real number.")

        if bmi <= 0:
            raise InvalidHealthDataException("BMI must be positive.")

        if bmi > 150:
            raise InvalidHealthDataException("BMI must be within a possible biological range [0-150].")

        if bmi < 16.0:
            return "Severe Thinness"

        if bmi < 17.0:
            return "Moderate Thinness"

        if bmi < 18.5:
            return "Mild Thinness"

        if bmi < 25.0:
            return "Normal"

        if bmi < 30.0:
            return "Overweight"

        if bmi < 35.0:
            return "Obesity Class I"

        if bmi < 40.0:
            return "Obesity Class II"

        return "Obesity Class III"


    #BMI CALCULATION

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


    #IBW

    def ibw(self, height: float, sex: str) -> float:

        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")

        if sex not in ["male", "female"]:
            raise InvalidHealthDataException("Sex must be 'male' or 'female'.")

        if sex == "male":
            return 50 + 0.9 * (height - 152.4)

        else:
            return 45.5 + 0.9 * (height - 152.4)


    #BMR

    def bmr(self, weight: float, height: float, age: int, sex: str) -> float:

        if weight <= 0:
            raise InvalidHealthDataException("Weight must be positive.")

        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")

        if age <= 0:
            raise InvalidHealthDataException("Age must be positive.")

        if sex not in ["male", "female"]:
            raise InvalidHealthDataException("Sex must be 'male' or 'female'.")

        if sex == "male":
            return (10 * weight) + (6.25 * height) - (5 * age) + 5

        else:
            return (10 * weight) + (6.25 * height) - (5 * age) - 161