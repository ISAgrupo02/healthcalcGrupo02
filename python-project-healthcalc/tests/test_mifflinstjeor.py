import pytest

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.gender import Gender
from healthcalc.person_impl import PersonImpl


class TestBMR:

    @pytest.fixture(autouse=True)
    def set_up(self):
        """Executed before each test."""
        self.health_calc = HealthCalcImpl()

    # --- BMR Calculation Tests (Mifflin-St Jeor) ---

    def test_bmr_valido_hombre(self):
        """Cálculo válido de BMR para hombre."""

        weight = 70.0
        height = 175.0
        age = 30

        person = PersonImpl(
            weight,
            height,
            Gender.MALE,
            age
        )

        expected_bmr = (
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            + 5
        )

        result = self.health_calc.bmr_person(person)

        assert result == pytest.approx(expected_bmr, abs=0.01)

    def test_bmr_valido_mujer(self):
        """Cálculo válido de BMR para mujer."""

        weight = 60.0
        height = 165.0
        age = 25

        person = PersonImpl(
            weight,
            height,
            Gender.FEMALE,
            age
        )

        expected_bmr = (
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            - 161
        )

        result = self.health_calc.bmr_person(person)

        assert result == pytest.approx(expected_bmr, abs=0.01)

    # --- Validation Tests ---

    def test_bmr_invalido_peso_negativo(self):
        """Negative weight should raise exception."""

        person = PersonImpl(
            -70.0,
            175.0,
            Gender.MALE,
            30
        )

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr_person(person)

    def test_bmr_peso_cero(self):
        """Zero weight should raise exception."""

        person = PersonImpl(
            0.0,
            175.0,
            Gender.MALE,
            30
        )

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr_person(person)

    def test_bmr_invalido_altura_negativa(self):
        """Negative height should raise exception."""

        person = PersonImpl(
            70.0,
            -175.0,
            Gender.MALE,
            30
        )

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr_person(person)

    def test_bmr_altura_cero(self):
        """Zero height should raise exception."""

        person = PersonImpl(
            70.0,
            0.0,
            Gender.MALE,
            30
        )

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr_person(person)