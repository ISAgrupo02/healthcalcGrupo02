from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.health_calc_adapter import HealthHospitalAdapter
from healthcalc.health_stats_proxy import HealthStatsProxy
from healthcalc.health_hospital_decorator import HealthHospitalDecorator
from healthcalc.health_hospital_internacional_decorator import InternationalHealthDecorator


def main():

    # ==================================================
    # PATRÓN SINGLETON
    # ==================================================

    print("==== PRUEBA SINGLETON ====")

    calc1 = HealthCalcImpl()
    calc2 = HealthCalcImpl()

    print("¿calc1 y calc2 son el mismo objeto?:", calc1 is calc2)

    # ==================================================
    # PATRÓN ADAPTER + PROXY
    # ==================================================

    print("\n==== PRUEBA ADAPTER + PROXY ====")

    calculadora = HealthCalcImpl()

    servicio = HealthHospitalAdapter(calculadora)

    hospital = HealthStatsProxy(servicio)

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

    # ==================================================
    # PATRÓN DECORATOR
    # ==================================================

    print("\n==== PRUEBA DECORATOR ====")

    # Decorator europeo/español
    calc_es = InternationalHealthDecorator(
        hospital,
        sistema="EU",
        idioma="ES"
    )

    # Decorator americano/inglés
    calc_en = InternationalHealthDecorator(
        hospital,
        sistema="US",
        idioma="EN"
    )

    print("\n=== EUROPEO / ESPAÑOL ===")

    imc_es, clas_es = calc_es.indiceMasaCorporal(1.83, 78000)

    print(f"IMC: {imc_es:.2f}")
    print(f"Clasificación: {clas_es}")

    print("\n=== AMERICANO / INGLÉS ===")

    imc_en, clas_en = calc_en.indiceMasaCorporal(72, 171)

    print(f"BMI: {imc_en:.2f}")
    print(f"Classification: {clas_en}")

    # ==================================================
    # ESTADÍSTICAS FINALES
    # ==================================================

    print("\n==== ESTADÍSTICAS FINALES ====")

    print(f"Pacientes totales: {hospital.numTotalPacientes()}")
    print(f"Altura media: {hospital.alturaMedia():.2f} m")
    print(f"Peso medio: {hospital.pesoMedio():.2f} kg")
    print(f"IMC medio: {hospital.imcMedio():.2f}")


if __name__ == "__main__":
    main()