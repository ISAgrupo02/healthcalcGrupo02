from .health_hospital_decorator import HealthHospitalDecorator


class InternationalHealthDecorator(HealthHospitalDecorator):

    def __init__(self, servicio, sistema="EU", idioma="ES"):
        super().__init__(servicio)

        self.sistema = sistema
        self.idioma = idioma

    def indiceMasaCorporal(self, altura: float, peso: int):

        altura_original = altura
        peso_original = peso

        # Convertir a sistema métrico si es necesario
        if self.sistema == "US":
            altura = altura / 39.37
            peso = int((peso / 2.20462) * 1000)

        imc, clasificacion = self.servicio.indiceMasaCorporal(altura, peso)

        
        if self.idioma == "ES":
            print(
                f"La persona con altura {altura_original} "
                f"y peso {peso_original} tiene un IMC de {imc:.2f}"
            )

        else:
            print(
                f"The person with height {altura_original} "
                f"and weight {peso_original} has a BMI of {imc:.2f}"
            )

        return imc, clasificacion