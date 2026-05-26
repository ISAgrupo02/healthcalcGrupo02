from behave import given, then
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


@given('que el sistema HealthCalc está operativo')
def step_sistema_operativo(context):
    context.calc = HealthCalcImpl()
    context.bmi = None
    context.resultado = None
    context.excepcion = None


@then('el sistema debe lanzar la excepción "{excepcion_esperada}"')
def step_excepcion(context, excepcion_esperada):
    assert context.excepcion is not None
    assert excepcion_esperada in str(type(context.excepcion).__name__)
