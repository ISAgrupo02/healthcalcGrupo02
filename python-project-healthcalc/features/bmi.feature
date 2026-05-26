# language: es

Característica: Cálculo del índice de masa corporal (BMI)

  Como usuario de la calculadora de salud
  Quiero calcular mi índice de masa corporal
  Para conocer si mi peso está en un rango adecuado según mi altura

Antecedentes:
  Dado que el sistema HealthCalc está operativo

Escenario: Cálculo válido del BMI
  Dado que el peso es 70.0 kg
  Y la altura es 1.75 m

  Cuando el sistema calcula el índice de masa corporal
  
  Entonces el resultado debe coincidir con la fórmula del BMI

Escenario: Cálculo válido del BMI con otro valor
  Dado que el peso es 55.0 kg
  Y la altura es 1.60 m
  
  Cuando el sistema calcula el índice de masa corporal
  
  Entonces el resultado debe coincidir con la fórmula del BMI

Escenario: Peso negativo
  Dado que el peso es -70.0 kg
  
  Y la altura es 1.75 m
  
  Cuando el sistema calcula el índice de masa corporal
  Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"

Escenario: Peso igual a cero
  Dado que el peso es 0.0 kg
  
  Y la altura es 1.65 m
  
  Cuando el sistema calcula el índice de masa corporal
  Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"

Escenario: Altura negativa
  Dado que el peso es 70.0 kg
  Y la altura es -1.75 m
  
  Cuando el sistema calcula el índice de masa corporal
  
  Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"

Escenario: Altura igual a cero
  Dado que el peso es 70.0 kg
  Y la altura es 0.0 m
  
  Cuando el sistema calcula el índice de masa corporal
  
  Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"