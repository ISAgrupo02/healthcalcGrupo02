import pytest

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.gender import Gender
from healthcalc.person_impl import PersonImpl


class TestIBW:

    @pytest.fixture(autouse=True)
    def set_up(self):
        """Executed before each test."""
        self.health_calc = HealthCalcImpl()

    # --- IBW Calculation Tests ---

    def test_ibw_valido_hombre(self):
        """Cálculo válido de IBW para hombre."""

        height = 175.0

        person = PersonImpl(
            70.0,
            height,
            Gender.MALE,
            30
        )

        expected_ibw = 50 + 0.9 * (height - 152.4)

        result = self.health_calc.ibw_person(person)

        assert result == expected_ibw

    def test_ibw_valido_mujer(self):
        """Cálculo válido de IBW para mujer."""

        height = 160.0

        person = PersonImpl(
            60.0,
            height,
            Gender.FEMALE,
            25
        )

        expected_ibw = 45.5 + 0.9 * (height - 152.4)

        result = self.health_calc.ibw_person(person)

        assert result == expected_ibw

    # --- Validation Tests ---

    def test_ibw_invalido_altura_negativa(self):
        """Negative height should raise exception."""

        person = PersonImpl(
            60.0,
            -160.0,
            Gender.FEMALE,
            25
        )

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw_person(person)

    def test_ibw_altura_cero(self):
        """Zero height should raise exception."""

        person = PersonImpl(
            60.0,
            0.0,
            Gender.FEMALE,
            25
        )

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw_person(person)

    def test_ibw_invalido_sexo(self):
        """Invalid sex should raise exception."""

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.ibw(160.0, "other")