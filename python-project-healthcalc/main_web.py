from flask import Flask, render_template, request, redirect, url_for

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException

app = Flask(__name__)


@app.route('/')
def menu():
    return redirect(url_for('ibw'))


@app.route('/ibw', methods=['GET', 'POST'])
def ibw():
    result = None
    error = None
    height = ''
    weight = ''
    age = ''
    sex = ''

    if request.method == 'POST':
        height = request.form.get('height', '').strip()
        sex = request.form.get('sex', '').strip()

        try:
            if sex == '':
                raise ValueError("sexo")

            if height == '':
                raise ValueError("altura_vacia")

            height_value = float(height)

            if height_value <= 0:
                raise InvalidHealthDataException("La altura debe ser positiva.")

            calc = HealthCalcImpl()
            result = calc.ibw(height_value, sex)

        except ValueError as e:
            if str(e) == "sexo":
                error = "Debe seleccionar un sexo."
            elif str(e) == "altura_vacia":
                error = "Debe introducir una altura."
            else:
                error = "La altura debe ser un número válido."

        except InvalidHealthDataException:
            error = "La altura debe ser positiva."

    return render_template(
        'index.html',
        result=result,
        error=error,
        height=height,
        weight=weight,
        age=age,
        sex=sex,
        active_page='ibw'
    )


@app.route('/mifflin', methods=['GET', 'POST'])
def mifflin():
    result = None
    error = None
    height = ''
    weight = ''
    age = ''
    sex = ''

    if request.method == 'POST':
        height = request.form.get('height', '').strip()
        weight = request.form.get('weight', '').strip()
        age = request.form.get('age', '').strip()
        sex = request.form.get('sex', '').strip()

        try:
            if sex == '':
                raise ValueError("sexo")

            if height == '':
                raise ValueError("altura_vacia")

            if weight == '':
                raise ValueError("peso_vacio")

            if age == '':
                raise ValueError("edad_vacia")

            height_value = float(height)
            weight_value = float(weight)
            age_value = int(age)

            if weight_value < 0:
                raise InvalidHealthDataException("El peso debe de tener un valor positivo")

            if weight_value == 0:
                raise InvalidHealthDataException("El peso debe de tener un valor positivo mayor que 0")

            if height_value == 0:
                raise InvalidHealthDataException("La altura debe de tener un valor positivo mayor que 0")

            if height_value < 0:
                raise InvalidHealthDataException("La altura debe de tener un valor positivo")

            if age_value <= 0:
                raise InvalidHealthDataException("La edad debe de tener un valor positivo mayor que 0")

            calc = HealthCalcImpl()
            result = calc.bmr(weight_value, height_value, age_value, sex)

        except ValueError as e:
            if str(e) == "sexo":
                error = "Debe seleccionar un sexo."
            elif str(e) == "altura_vacia":
                error = "Debe introducir una altura."
            elif str(e) == "peso_vacio":
                error = "Debe introducir un peso."
            elif str(e) == "edad_vacia":
                error = "Debe introducir una edad."
            else:
                error = "Altura, peso y edad deben ser valores numéricos válidos."

        except InvalidHealthDataException as e:
            error = str(e)

    return render_template(
        'index.html',
        result=result,
        error=error,
        height=height,
        weight=weight,
        age=age,
        sex=sex,
        active_page='mifflin'
    )


@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    result = None
    classification = None
    error = None
    height = ''
    weight = ''
    age = ''
    sex = ''

    if request.method == 'POST':
        height = request.form.get('height', '').strip()
        weight = request.form.get('weight', '').strip()

        try:
            if height == '':
                raise ValueError("altura_nula")

            if weight == '':
                raise ValueError("peso_nulo")

            height_value = float(height)
            weight_value = float(weight)

            if height_value <= 0:
                raise InvalidHealthDataException("La altura no puede ser nula o negativa.")

            if weight_value <= 0:
                raise InvalidHealthDataException("El peso no puede ser nulo o negativo.")

            result = weight_value / (height_value ** 2)

            if result < 18.5:
                classification = "Bajo peso"
            elif result < 25:
                classification = "Peso normal"
            elif result < 30:
                classification = "Sobrepeso"
            else:
                classification = "Obesidad"

        except ValueError as e:
            if str(e) == "altura_nula":
                error = "La altura no puede ser nula."
            elif str(e) == "peso_nulo":
                error = "El peso no puede ser nulo."
            else:
                error = "Altura y peso deben ser números válidos."

        except InvalidHealthDataException as e:
            error = str(e)

    return render_template(
        'index.html',
        result=result,
        classification=classification,
        error=error,
        height=height,
        weight=weight,
        age=age,
        sex=sex,
        active_page='bmi'
    )


if __name__ == '__main__':
    app.run(debug=True)