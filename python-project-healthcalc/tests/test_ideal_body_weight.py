import pytest

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.person_impl import PersonImpl
from healthcalc.gender import Gender


class TestIdealBodyWeight:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.health_calc = HealthCalcImpl()

    def test_ideal_body_weight_hombre(self):

        person = PersonImpl(
            weight=70.0,
            height=175.0,
            gender=Gender.MALE,
            age=30
        )

        result = self.health_calc.ideal_body_weight(person)

        expected = 50 + 0.9 * (175.0 - 152.4)

        assert result == expected