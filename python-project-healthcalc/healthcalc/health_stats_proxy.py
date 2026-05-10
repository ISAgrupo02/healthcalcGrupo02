from .health_stats import HealthStats
from .health_calc_interface import HealthHospital


class HealthStatsProxy(HealthStats):

    def __init__(self, servicio: HealthHospital):
        self.servicio = servicio
        self.totalAltura = 0.0
        self.totalPeso = 0.0
        self.totalIMC = 0.0
        self.totalPacientes = 0
        self.numHombres = 0
        self.numMujeres = 0

    def indiceMasaCorporal(self, altura: float, peso: float, genero: str) -> tuple[float, str]:
        imc, clasificacion = self.servicio.indiceMasaCorporal(altura, peso)

        self.totalAltura += altura
        self.totalPeso += peso
        self.totalIMC += imc
        self.totalPacientes += 1

        if genero.upper() == "H":
            self.numHombres += 1
        elif genero.upper() == "M":
            self.numMujeres += 1
        else:
            raise ValueError("Error: genero debe ser 'H' o 'M'.")

        return imc, clasificacion

    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        return self.servicio.pesoCorporalIdeal(genero, altura)

    def alturaMedia(self) -> float:
        if self.totalPacientes == 0:
            return 0.0
        return self.totalAltura / self.totalPacientes

    def pesoMedio(self) -> float:
        if self.totalPacientes == 0:
            return 0.0
        return self.totalPeso / self.totalPacientes

    def imcMedio(self) -> float:
        if self.totalPacientes == 0:
            return 0.0
        return self.totalIMC / self.totalPacientes

    def numSexo(self, genero: str) -> int:
        if genero.upper() == "H":
            return self.numHombres
        elif genero.upper() == "M":
            return self.numMujeres
        else:
            raise ValueError("Error: genero debe ser 'H' o 'M'.")

    def numTotalPacientes(self) -> int:
        return self.totalPacientes