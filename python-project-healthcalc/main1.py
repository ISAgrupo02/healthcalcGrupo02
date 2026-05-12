from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.health_calc_adapter import HealthHospitalAdapter
from healthcalc.health_stats_proxy import HealthStatsProxy


def main():
    print("==== PRUEBA SINGLETON ====")

    calc1 = HealthCalcImpl()
    calc2 = HealthCalcImpl()

    print("¿calc1 y calc2 son el mismo objeto?", calc1 is calc2)

    print("\n==== PRUEBA ADAPTER + PROXY ====")

    calculadora = HealthCalcImpl()
    adapter = HealthHospitalAdapter(calculadora)
    hospital = HealthStatsProxy(adapter)

    imc, clasificacion = hospital.indiceMasaCorporal(1.83, 78000)
    peso_ideal = hospital.pesoCorporalIdeal("H", 1.83)

    print(f"IMC: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")
    print(f"Peso ideal: {peso_ideal} kg")

    print("\n==== ESTADÍSTICAS ====")
    print(f"Altura media: {hospital.alturaMedia():.2f} m")
    print(f"Peso medio: {hospital.pesoMedio():.2f} kg")
    print(f"IMC medio: {hospital.imcMedio():.2f}")
    print(f"Hombres: {hospital.numSexo('H')}")
    print(f"Total pacientes: {hospital.numTotalPacientes()}")


if __name__ == "__main__":
    main()