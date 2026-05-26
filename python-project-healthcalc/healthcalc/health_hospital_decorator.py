from .health_hospital_interface import HealthHospital


class HealthHospitalDecorator(HealthHospital):

    def __init__(self, servicio: HealthHospital):
        self.servicio = servicio

    def indiceMasaCorporal(self, altura: float, peso: int):
        return self.servicio.indiceMasaCorporal(altura, peso)

    def pesoCorporalIdeal(self, genero: str, altura: float):
        return self.servicio.pesoCorporalIdeal(genero, altura)