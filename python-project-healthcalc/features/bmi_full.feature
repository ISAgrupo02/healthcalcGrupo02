# language: es

Característica: Clasificación completa del índice de masa corporal (BMI Full)

  Como usuario de la calculadora de salud
  Quiero conocer la clasificación completa de mi índice de masa corporal
  Para entender mejor mi estado nutricional

  Antecedentes:
    Dado que el sistema HealthCalc está operativo

  Esquema del escenario: Clasificación correcta del BMI Full
    Dado que el BMI es <bmi>
    Cuando el sistema realiza la clasificación completa del BMI
    Entonces el resultado debe ser "<clasificacion>"

    Ejemplos:
      | bmi   | clasificacion       |
      | 15.9  | Severe Thinness     |
      | 16.0  | Moderate Thinness   |
      | 17.0  | Mild Thinness       |
      | 18.5  | Normal              |
      | 25.0  | Overweight          |
      | 30.0  | Obesity Class I     |
      | 35.0  | Obesity Class II    |
      | 40.0  | Obesity Class III   |
      | 150.0 | Obesity Class III   |

  Esquema del escenario: BMI inválido por valor no permitido
    Dado que el BMI es <bmi_invalido>
    Cuando el sistema realiza la clasificación completa del BMI
    Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"

    Ejemplos:
      | bmi_invalido |
      | -1.0         |
      | 0.0          |
      | 150.1        |

  Esquema del escenario: BMI no es un número real finito
    Dado que el BMI no finito es "<valor>"
    Cuando el sistema realiza la clasificación completa del BMI
    Entonces el sistema debe lanzar la excepción "InvalidHealthDataException"

    Ejemplos:
      | valor    |
      | NaN      |
      | Infinity |
      | -Infinity |
