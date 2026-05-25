import pytest

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.gender import Gender
from healthcalc.person_impl import PersonImpl
from healthcalc.person_impl import PersonImpl
from healthcalc.gender import Gender


class TestIBW:

    @pytest.fixture(autouse=True)
    def set_up(self):
        """Executed before each test."""
        self.health_calc = HealthCalcImpl()

    # --- IBW Calculation Tests ---

    def test_ibw_valido_hombre(self):
        height = 175.0

        person = PersonImpl(
           weight=70.0,
           height=height,
           gender=Gender.MALE,
           age=30
        )

        expected_ibw = 50 + 0.9 * (height - 152.4)
        result = self.health_calc.ideal_body_weight(person)

        assert result == expected_ibw

    def test_ibw_valido_mujer(self):
        height = 160.0

        person = PersonImpl(
           weight=60.0,
           height=height,
           gender=Gender.FEMALE,
           age=25
       )

        expected_ibw = 45.5 + 0.9 * (height - 152.4)
        result = self.health_calc.ideal_body_weight(person)

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