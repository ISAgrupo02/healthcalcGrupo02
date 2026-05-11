from healthcalc.health_calc_interface import HealthCalc


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class HealthCalcImp(HealthCalc, metaclass=MetaSingleton):

    def bmi(self, weight: float, height: float) -> float:
        if not isinstance(weight, (int, float)):
            raise TypeError("Error: weight debe ser un número.")
        if not isinstance(height, (int, float)):
            raise TypeError("Error: height debe ser un número.")
        if weight <= 0:
            raise ValueError("Error: weight debe ser mayor que 0.")
        if height <= 0:
            raise ValueError("Error: height debe ser mayor que 0.")

        return weight / (height ** 2)

    def bmi_classification(self, bmi: float) -> str:
        if not isinstance(bmi, (int, float)):
            raise TypeError("Error: bmi debe ser un número.")

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    def ibw(self, height: float, sex: str) -> float:
        if not isinstance(height, (int, float)):
            raise TypeError("Error: height debe ser un número.")
        if height <= 0:
            raise ValueError("Error: height debe ser mayor que 0.")

        sex = sex.lower()

        # height en centímetros
        inches = height / 2.54

        if sex == "male" or sex == "m":
            return 50 + 2.3 * (inches - 60)
        elif sex == "female" or sex == "f":
            return 45.5 + 2.3 * (inches - 60)
        else:
            raise ValueError("Error: sex debe ser 'male', 'female', 'm' o 'f'.")

    def bmr(self, weight: float, height: float, age: int, sex: str) -> float:
        if weight <= 0:
            raise ValueError("Error: weight debe ser mayor que 0.")
        if height <= 0:
            raise ValueError("Error: height debe ser mayor que 0.")
        if age <= 0:
            raise ValueError("Error: age debe ser mayor que 0.")

        sex = sex.lower()

        # Fórmula Mifflin-St Jeor
        if sex == "male" or sex == "m":
            return 10 * weight + 6.25 * height - 5 * age + 5
        elif sex == "female" or sex == "f":
            return 10 * weight + 6.25 * height - 5 * age - 161
        else:
            raise ValueError("Error: sex debe ser 'male', 'female', 'm' o 'f'.")