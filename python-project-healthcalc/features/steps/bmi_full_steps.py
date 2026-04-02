from behave import given, when, then
from math import inf, nan

from healthcalc.exceptions import InvalidHealthDataException


@given('que el BMI es {bmi:f}')
def step_bmi_valido(context, bmi):
    context.bmi = bmi


@given('que el BMI no finito es "{valor}"')
def step_bmi_no_finito(context, valor):
    if valor == "NaN":
        context.bmi = nan
    elif valor == "Infinity":
        context.bmi = inf
    elif valor == "-Infinity":
        context.bmi = -inf
    else:
        raise ValueError(f"Valor no soportado en el feature: {valor}")


@when('el sistema realiza la clasificación completa del BMI')
def step_clasificacion_bmi_full(context):
    try:
        context.resultado = context.calc.bmi_full_classification(context.bmi)
        context.excepcion = None
    except Exception as e:
        context.resultado = None
        context.excepcion = e


@then('el resultado debe ser "{clasificacion}"')
def step_resultado_clasificacion(context, clasificacion):
    assert context.excepcion is None, (
        f"No se esperaba excepción, pero se lanzó: {context.excepcion}"
    )
    assert context.resultado == clasificacion, (
        f"Se esperaba '{clasificacion}', pero se obtuvo '{context.resultado}'"
    )