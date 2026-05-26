from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException




@given('un peso aproximado de {peso:f} kg')
def step_peso_aproximado(context, peso):
    context.peso = peso


@given('un peso nulo de {peso:f} kg')
def step_peso_nulo(context, peso):
    context.peso = peso


@given('un peso de {peso:f} kg')
def step_peso(context, peso):
    context.peso = peso


@given('una altura aproximada de {altura:f} cm')
def step_altura_aproximada(context, altura):
    context.altura = altura


@given('una altura de {altura:f} cm')
def step_altura(context, altura):
    context.altura = altura


@given('una altura dada de {altura:f} cm')
def step_altura_dada(context, altura):
    context.altura = altura


@given('una altura nula de {altura:f} cm')
def step_altura_nula(context, altura):
    context.altura = altura


@given('una edad de {edad:d} años')
def step_edad(context, edad):
    context.edad = edad


@given('un sexo masculino "{sexo}"')
def step_sexo_masculino(context, sexo):
    context.sexo = sexo


@given('un sexo femenino "{sexo}"')
def step_sexo_femenino(context, sexo):
    context.sexo = sexo


@when('solicito calcular el BMR')
def step_calcular_bmr(context):
    try:
        context.resultado = context.calc.bmr(
            context.peso,
            context.altura,
            context.edad,
            context.sexo
        )
        context.excepcion = None
    except Exception as e:
        context.resultado = None
        context.excepcion = e


@then('el resultado del cálculo debe ser {esperado:f}')
def step_resultado(context, esperado):
    assert context.excepcion is None, f"Se produjo una excepción inesperada: {context.excepcion}"
    assert abs(context.resultado - esperado) < 0.01, \
        f"Esperado {esperado}, obtenido {context.resultado}"


@then('se debe mostrar por pantalla un error de datos inválidos')
def step_error_1(context):
    assert isinstance(context.excepcion, InvalidHealthDataException)


@then('se debe mostrar un error por pantalla de datos inválidos')
def step_error_2(context):
    assert isinstance(context.excepcion, InvalidHealthDataException)
