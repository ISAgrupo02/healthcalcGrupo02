from flask import Flask, render_template, request, redirect, url_for

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.health_calc_adapter import HealthHospitalAdapter
from healthcalc.health_stats_proxy import HealthStatsProxy
from healthcalc.health_hospital_internacional_decorator import InternationalHealthDecorator
from healthcalc.exceptions import InvalidHealthDataException

app = Flask(__name__)


stats_proxy = None
decorated_proxy = None


def get_stats_proxy():
    """
    Initialize proxy on first use (Lazy initialization pattern).
    Returns: Proxy instance that wraps the Adapter
    Pattern: Proxy -> Adapter -> HealthCalc (Singleton)
    """
    global stats_proxy
    if stats_proxy is None:
        calc = HealthCalcImpl.getInstance()  # Singleton instance
        adapter = HealthHospitalAdapter(calc)
        stats_proxy = HealthStatsProxy(adapter)
    return stats_proxy


def get_decorated_proxy(sistema="EU", idioma="ES"):
    """
    Get the Proxy wrapped with Decorator for internationalization.
    Pattern chain: Decorator -> Proxy -> Adapter -> HealthCalc (Singleton)
    """
    proxy = get_stats_proxy()
    decorated = InternationalHealthDecorator(proxy, sistema=sistema, idioma=idioma)
    return decorated


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

            
            adapter = HealthHospitalAdapter(HealthCalcImpl.getInstance())
            result = adapter.pesoCorporalIdeal(sex, height_value / 100)

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
                raise InvalidHealthDataException("El peso debe de tener un valor positivo")

            if height_value == 0:
                raise InvalidHealthDataException("La altura debe de tener un valor positivo")

            if height_value < 0:
                raise InvalidHealthDataException("La altura debe de tener un valor positivo")

            if age_value <= 0:
                raise InvalidHealthDataException("La edad debe de tener un valor positivo")

           
            calc = HealthCalcImpl.getInstance()
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
    sex = 'H'

    if request.method == 'POST':
        height = request.form.get('height', '').strip()
        weight = request.form.get('weight', '').strip()
        sex = request.form.get('sex', 'H').strip()
        sistema = request.form.get('sistema', 'EU').strip()
        idioma = request.form.get('idioma', 'ES').strip()

        try:
            if height == '':
                raise ValueError("altura_nula")

            if weight == '':
                raise ValueError("peso_nulo")

            height_value = float(height)
            weight_value = float(weight)

            if height_value <= 0:
                raise InvalidHealthDataException("La altura debe ser un valor positivo.")

            if weight_value <= 0:
                raise InvalidHealthDataException("El peso debe ser un valor positivo.")

            
            if sistema and idioma:
                decorated = get_decorated_proxy(sistema=sistema, idioma=idioma)
                result, classification = decorated.indiceMasaCorporal(
                    height_value, int(weight_value * 1000)  
                )
            else:
                
                proxy = get_stats_proxy()
                result, classification = proxy.indiceMasaCorporal(
                    height_value, int(weight_value * 1000)
                )

        except ValueError as e:
            if str(e) == "altura_nula":
                error = "Debe seleccionar una altura."
            elif str(e) == "peso_nulo":
                error = "Debe seleccionar un peso."
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


@app.route('/stats', methods=['GET'])
def stats():
    """
    Display statistics tracked by the Proxy pattern.
    Shows aggregated data from all calculations.
    """
    proxy = get_stats_proxy()
    stats_data = {
        'total_pacientes': proxy.totalPacientes,
        'altura_media': f"{proxy.alturaMedia():.2f}" if proxy.totalPacientes > 0 else "0.00",
        'peso_medio': f"{proxy.pesoMedio():.2f}" if proxy.totalPacientes > 0 else "0.00",
        'imc_medio': f"{proxy.imcMedio():.2f}" if proxy.totalPacientes > 0 else "0.00",
        'num_hombres': proxy.numHombres,
        'num_mujeres': proxy.numMujeres
    }
    return render_template('stats.html', stats=stats_data)


if __name__ == '__main__':
    app.run(debug=True)
