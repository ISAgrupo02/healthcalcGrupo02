import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.gender import Gender

class TestBMR:

    @pytest.fixture(autouse=True)
    def set_up(self):
        """Executed before each test."""
        self.health_calc = HealthCalcImpl()

    # --- BMR Calculation Tests (Mifflin-St Jeor) ---

    def test_bmr_valido_hombre(self):
        """Cálculo válido de BMR para hombre (Mifflin-St Jeor)."""

        # Arrange
        weight = 70.0      # kg
        height = 175.0     # cm
        age = 30           # years
        sex = Gender.MALE

        # Act
        expected_bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        result = self.health_calc.bmr(weight, height, age, sex)

        # Assert
        assert result == pytest.approx(expected_bmr, abs=0.01)

    def test_bmr_valido_mujer(self):
        """Cálculo válido de BMR para mujer (Mifflin-St Jeor)."""

        # Arrange
        weight = 60.0
        height = 165.0
        age = 25
        sex = Gender.FEMALE

        # Act
        expected_bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        result = self.health_calc.bmr(weight, height, age, sex)

        # Assert
        assert result == pytest.approx(expected_bmr, abs=0.01)

    # --- Validation Tests ---

    def test_bmr_invalido_peso_negativo(self):
        """Negative weight should raise exception."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(-70.0, 175.0, 30, Gender.MALE)

    def test_bmr_peso_cero(self):
        """Zero weight should raise exception."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(0.0, 175.0, 30, Gender.MALE)

    def test_bmr_invalido_altura_negativa(self):
        """Negative height should raise exception."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(70.0, -175.0, 30, Gender.MALE)

    def test_bmr_altura_cero(self):
        """Zero height should raise exception."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(70.0, 0.0, 30, Gender.MALE)