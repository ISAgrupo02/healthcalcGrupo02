# main.py

import argparse

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


def main():
    """
    Entry point of the HealthCalc application.
    Allows testing health metrics from the command line.
    """

    parser = argparse.ArgumentParser(
        description="HealthCalc CLI - Calculate health metrics from terminal"
    )

    subparsers = parser.add_subparsers(dest="metric")

    #BMI
    bmi_parser = subparsers.add_parser("bmi", help="Calculate BMI")
    bmi_parser.add_argument("--weight", type=float, required=True, help="Weight in kg")
    bmi_parser.add_argument("--height", type=float, required=True, help="Height in meters")

    #BMI BASIC CLASSIFICATION 
    bmi_class_parser = subparsers.add_parser("bmi-class", help="BMI basic classification")
    bmi_class_parser.add_argument("--bmi", type=float, required=True)

    #BMI FULL CLASSIFICATION
    bmi_full_parser = subparsers.add_parser("bmi-full", help="BMI full classification")
    bmi_full_parser.add_argument("--bmi", type=float, required=True)

    #IBW
    ibw_parser = subparsers.add_parser("ibw", help="Calculate Ideal Body Weight")
    ibw_parser.add_argument("--height", type=float, required=True, help="Height in cm")
    ibw_parser.add_argument("--sex", type=str, required=True, choices=["male", "female"])

    #BMR
    bmr_parser = subparsers.add_parser("bmr", help="Calculate Basal Metabolic Rate")
    bmr_parser.add_argument("--weight", type=float, required=True)
    bmr_parser.add_argument("--height", type=float, required=True)
    bmr_parser.add_argument("--age", type=int, required=True)
    bmr_parser.add_argument("--sex", type=str, required=True, choices=["male", "female"])

    args = parser.parse_args()

    calc = HealthCalcImpl()

    try:

        if args.metric == "bmi":
            result = calc.bmi(args.weight, args.height)
            print(f"BMI = {result:.2f}")

        elif args.metric == "bmi-class":
            result = calc.bmi_classification(args.bmi)
            print(f"BMI Classification = {result}")

        elif args.metric == "bmi-full":
            result = calc.bmi_full_classification(args.bmi)
            print(f"BMI FULL Classification = {result}")

        elif args.metric == "ibw":
            result = calc.ibw(args.height, args.sex)
            print(f"Ideal Body Weight = {result:.2f} kg")

        elif args.metric == "bmr":
            result = calc.bmr(args.weight, args.height, args.age, args.sex)
            print(f"BMR = {result:.2f} kcal/day")

        else:
            parser.print_help()

    except InvalidHealthDataException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()