# main.py

import argparse

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.health_calc_adapter import HealthHospitalAdapter
from healthcalc.health_stats_proxy import HealthStatsProxy
from healthcalc.health_hospital_internacional_decorator import InternationalHealthDecorator
from healthcalc.exceptions import InvalidHealthDataException



_health_proxy = None


def get_health_proxy():
   
    global _health_proxy
    if _health_proxy is None:
       
        calc = HealthCalcImpl.getInstance()  
        adapter = HealthHospitalAdapter(calc)
        _health_proxy = HealthStatsProxy(adapter)
    return _health_proxy


def get_decorated_proxy(sistema="EU", idioma="ES"):

    proxy = get_health_proxy()

    decorated = InternationalHealthDecorator(proxy, sistema=sistema, idioma=idioma)
    return decorated


def main():


    parser = argparse.ArgumentParser(
        description="HealthCalc CLI - Calculate health metrics from terminal"
    )

    subparsers = parser.add_subparsers(dest="metric")

    # BMI
    bmi_parser = subparsers.add_parser("bmi", help="Calculate BMI")
    bmi_parser.add_argument("--weight", type=float, required=True, help="Weight in kg")
    bmi_parser.add_argument("--height", type=float, required=True, help="Height in meters")
    bmi_parser.add_argument("--international", type=str, choices=["EU", "US"], default="EU", 
                           help="Measurement system (EU=metric, US=imperial)")
    bmi_parser.add_argument("--idioma", type=str, choices=["ES", "EN"], default="ES", 
                           help="Language (ES=Spanish, EN=English)")

    # BMI BASIC CLASSIFICATION 
    bmi_class_parser = subparsers.add_parser("bmi-class", help="BMI basic classification")
    bmi_class_parser.add_argument("--bmi", type=float, required=True)

    # BMI FULL CLASSIFICATION
    bmi_full_parser = subparsers.add_parser("bmi-full", help="BMI full classification")
    bmi_full_parser.add_argument("--bmi", type=float, required=True)

    # IBW
    ibw_parser = subparsers.add_parser("ibw", help="Calculate Ideal Body Weight")
    ibw_parser.add_argument("--height", type=float, required=True, help="Height in cm")
    ibw_parser.add_argument("--sex", type=str, required=True, choices=["male", "female"])
    ibw_parser.add_argument("--international", type=str, choices=["H", "M"], default="H",
                           help="Gender format (H=Hombre, M=Mujer for adapter)")

    # BMR
    bmr_parser = subparsers.add_parser("bmr", help="Calculate Basal Metabolic Rate")
    bmr_parser.add_argument("--weight", type=float, required=True)
    bmr_parser.add_argument("--height", type=float, required=True)
    bmr_parser.add_argument("--age", type=int, required=True)
    bmr_parser.add_argument("--sex", type=str, required=True, choices=["male", "female"])

    
    stats_parser = subparsers.add_parser("stats", help="Show collected health statistics")

    args = parser.parse_args()

    calc = HealthCalcImpl.getInstance()  
    
    try:
        if args.metric == "bmi":
            if hasattr(args, 'international') and hasattr(args, 'idioma'):
                decorated = get_decorated_proxy(sistema=args.international, idioma=args.idioma)
                result, classification = decorated.indiceMasaCorporal(
                    args.height, int(args.weight * 1000) 
                )
                print(f"BMI = {result:.2f}")
                print(f"Classification = {classification}")
            else:
                result = calc.bmi(args.weight, args.height)
                print(f"BMI = {result:.2f}")

        elif args.metric == "bmi-class":
            
            result = calc.bmi_classification(args.bmi)
            print(f"BMI Classification = {result}")

        elif args.metric == "bmi-full":
            
            result = calc.bmi_full_classification(args.bmi)
            print(f"BMI FULL Classification = {result}")

        elif args.metric == "ibw":
            
            if hasattr(args, 'international'):
                adapter = HealthHospitalAdapter(calc)
                result = adapter.pesoCorporalIdeal(args.international, args.height / 100)
                print(f"Ideal Body Weight = {result} kg")
            else:
                result = calc.ibw(args.height, args.sex)
                print(f"Ideal Body Weight = {result:.2f} kg")

        elif args.metric == "bmr":
     
            result = calc.bmr(args.weight, args.height, args.age, args.sex)
            print(f"BMR = {result:.2f} kcal/day")

        elif args.metric == "stats":
            
            proxy = get_health_proxy()
            print("\n=== Health Statistics ===")
            print(f"Total Patients: {proxy.totalPacientes}")
            print(f"Average Height: {proxy.alturaMedia():.2f} m")
            print(f"Average Weight: {proxy.pesoMedio():.2f} kg")
            print(f"Average BMI: {proxy.imcMedio():.2f}")
            print(f"Men: {proxy.numHombres}")
            print(f"Women: {proxy.numMujeres}")

        else:
            parser.print_help()

    except InvalidHealthDataException as e:
        print("Error:", e)
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()