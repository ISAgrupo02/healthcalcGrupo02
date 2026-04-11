from flask import Flask, render_template, request

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None
    height = ''
    sex = ''

    if request.method == 'POST':
        height = request.form.get('height', '')
        sex = request.form.get('sex', '')

        try:
            # validar sexo vacío
            if sex == '':
                raise ValueError("sexo")

            # validar altura vacía
            if height == '':
                raise ValueError("altura")

            calc = HealthCalcImpl()
            result = calc.ibw(float(height), sex)

        except ValueError as e:
            if str(e) == "sexo":
                error = "Debe seleccionar un sexo."
            else:
                error = "La altura debe ser un número válido."

        except InvalidHealthDataException:
            error = "La altura debe ser positiva."

    return render_template(
        'index.html',
        result=result,
        error=error,
        height=height,
        sex=sex
    )


if __name__ == '__main__':
    app.run(debug=True)