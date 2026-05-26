from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


@given('que el peso es {peso:f} kg')
def step_peso(context, peso):
    context.peso = peso


@given('la altura es {altura:f} m')
def step_altura(context, altura):
    context.altura = altura


@when('el sistema calcula el índice de masa corporal')
def step_calcular_bmi(context):
    try:
        context.resultado = context.calc.bmi(context.peso, context.altura)
        context.excepcion = None
    except Exception as e:
        context.resultado = None
        context.excepcion = e


@then('el resultado debe coincidir con la fórmula del BMI')
def step_resultado_bmi(context):
    esperado = context.peso / (context.altura ** 2)
    assert abs(context.resultado - esperado) < 0.01