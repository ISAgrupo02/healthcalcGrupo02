class InternationalHealthDecorator(HealthHospitalDecorator):

    def __init__(self, servicio, sistema="EU", idioma="ES"):
        super().__init__(servicio)
        self.sistema = sistema
        self.idioma = idioma

    def indiceMasaCorporal(self, altura: float, peso: int):
        altura_original = altura
        peso_original = peso

        if self.sistema == "US":
            altura = altura / 39.37
            peso = int((peso / 2.20462) * 1000)

        imc, clasificacion = self.servicio.indiceMasaCorporal(altura, peso)

        if self.idioma == "ES":
            print(
                f"La persona con altura {altura_original} y peso {peso_original} "
                f"tiene un IMC de {imc:.2f}"
            )
        else:
            print(
                f"The person with height {altura_original} and weight {peso_original} "
                f"has a BMI of {imc:.2f}"
            )

        return imc, clasificacion