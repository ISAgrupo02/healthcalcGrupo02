# language: es

Característica: Cálculo de la tasa metabólica basal Mifflin-St Jeor (BMR)

  Como usuario de la calculadora de salud
  Quiero calcular mi tasa metabólica basal usando la fórmula Mifflin-St Jeor
  Para estimar las calorías mínimas en reposo

  Antecedentes:
    Dado que el sistema HealthCalc está operativo

  Escenario: Calcular BMR válido para un hombre
    Dado un peso aproximado de 70.0 kg
    Y una altura aproximada de 175.0 cm
    Y una edad de 30 años
    Y un sexo masculino "male"
    Cuando solicito calcular el BMR
    Entonces el resultado del cálculo debe ser 1648.75

  Escenario: Calcular BMR válido para una mujer
    Dado un peso aproximado de 60.0 kg
    Y una altura aproximada de 165.0 cm
    Y una edad de 25 años
    Y un sexo femenino "female"
    Cuando solicito calcular el BMR
    Entonces el resultado del cálculo debe ser 1345.25

  Escenario: Error con peso negativo
    Dado un peso aproximado de -70.0 kg
    Y una altura aproximada de 175.0 cm
    Y una edad de 30 años
    Y un sexo masculino "male"
    Cuando solicito calcular el BMR
    Entonces se debe mostrar por pantalla un error de datos inválidos

  Escenario: Error con peso nulo
    Dado un peso nulo de 0.0 kg
    Y una altura de 175.0 cm
    Y una edad de 30 años
    Y un sexo masculino "male"
    Cuando solicito calcular el BMR
    Entonces se debe mostrar por pantalla un error de datos inválidos

  Escenario: Error con altura negativa
    Dado un peso aproximado de 70.0 kg
    Y una altura dada de -175.0 cm
    Y una edad de 30 años
    Y un sexo masculino "male"
    Cuando solicito calcular el BMR
    Entonces se debe mostrar por pantalla un error de datos inválidos

  Escenario: Error con altura nula
    Dado un peso de 70.0 kg
    Y una altura nula de 0.0 cm
    Y una edad de 30 años
    Y un sexo masculino "male"
    Cuando solicito calcular el BMR
    Entonces se debe mostrar por pantalla un error de datos inválidos
