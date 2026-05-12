from .health_hospital_interface import HealthHospital
from .health_calc import HealthCalc

class HealthHospitalAdapter(HealthHospital):

   
    def __init__(self, calculadora: HealthCalc):
        self.calculadora = calculadora


    def indiceMasaCorporal(self, altura: float, peso: int) -> tuple[float, str]:
        peso_kg = peso / 1000

        bmi = self.calculadora.bmi(peso_kg, altura)
        clasificacion = self.calculadora.bmi_classification(bmi)

        return bmi, clasificacion

    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        altura_cm = altura * 100

        if genero.upper() == "H":
            sexo = "male"
        elif genero.upper() == "M":
            sexo = "female"
        else:
            raise ValueError("Error: genero debe ser 'H' o 'M'.")

        return int(self.calculadora.ibw(altura_cm, sexo))