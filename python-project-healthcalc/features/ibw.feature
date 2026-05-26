# language: es

Característica: Cálculo del peso corporal ideal (IBW)

  Como usuario de la calculadora de salud
  Quiero calcular mi peso corporal ideal
  Para conocer un peso recomendado según mi altura y sexo


Antecedentes:
  Dado que el sistema HealthCalc está operativo


Escenario: Cálculo válido del IBW para hombre

  Dado que la altura es 175 cm
  Y el sexo es "male"

  Cuando el sistema calcula el peso corporal ideal

  Entonces el resultado debe coincidir con la fórmula de IBW para hombres


Escenario: Cálculo válido del IBW para mujer

  Dado que la altura es 160 cm
  Y el sexo es "female"

  Cuando el sistema calcula el peso corporal ideal

  Entonces el resultado debe coincidir con la fórmula de IBW para mujeres


Escenario: Altura negativa

  Dado que la altura es -170 cm
  Y el sexo es "male"

  Cuando el sistema calcula el peso corporal ideal

  Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"


Escenario: Altura igual a cero

  Dado que la altura es 0 cm
  Y el sexo es "female"

  Cuando el sistema calcula el peso corporal ideal

  Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"


Escenario: Sexo inválido

  Dado que la altura es 170 cm
  Y el sexo es "other"

  Cuando el sistema calcula el peso corporal ideal

  Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"
