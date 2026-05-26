from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


@given('que la altura es {altura:d} cm')
def step_altura(context, altura):
    context.altura = altura


@given('el sexo es "{sexo}"')
def step_sexo(context, sexo):
    context.sexo = sexo


@when('el sistema calcula el peso corporal ideal')
def step_calcular_ibw(context):
    try:
        context.resultado = context.calc.ibw(context.altura, context.sexo)
        context.excepcion = None
    except Exception as e:
        context.resultado = None
        context.excepcion = e


@then('el resultado debe coincidir con la fórmula de IBW para hombres')
def step_resultado_hombre(context):
    esperado = 50 + 0.9 * (context.altura - 152.4)
    assert abs(context.resultado - esperado) < 0.01


@then('el resultado debe coincidir con la fórmula de IBW para mujeres')
def step_resultado_mujer(context):
    esperado = 45.5 + 0.9 * (context.altura - 152.4)
    assert abs(context.resultado - esperado) < 0.01