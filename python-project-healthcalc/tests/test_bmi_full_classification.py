import math
import pytest

from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


class TestBMIFullClassification:

    @pytest.fixture(autouse=True)  # Equivalent to @BeforeEach in JUnit
    def set_up(self):
        """Runs before each test."""
        self.health_calc = HealthCalcImpl()

    #Tests for FULL BMI classification

    @pytest.mark.parametrize("bmi", [10.0, 15.9, 15.99], ids=lambda x: f"BMI {x} -> Severe Thinness")
    def test_bmi_full_severe_thinness(self, bmi: float):
        """FULL BMI classification for Severe Thinness (bmi < 16.0)."""
        # Arrange (input provided by parametrization)

        # Act
        result = self.health_calc.bmi_full_classification(bmi)

        # Assert
        assert result == "Severe Thinness"

    @pytest.mark.parametrize("bmi", [16.0, 16.1, 16.9, 16.99], ids=lambda x: f"BMI {x} -> Moderate Thinness")
    def test_bmi_full_moderate_thinness(self, bmi: float):
        """FULL BMI classification for Moderate Thinness (16.0 <= bmi < 17.0)."""
        # Act
        result = self.health_calc.bmi_full_classification(bmi)

        # Assert
        assert result == "Moderate Thinness"

    @pytest.mark.parametrize("bmi", [17.0, 17.1, 18.4, 18.49], ids=lambda x: f"BMI {x} -> Mild Thinness")
    def test_bmi_full_mild_thinness(self, bmi: float):
        """FULL BMI classification for Mild Thinness (17.0 <= bmi < 18.5)."""
        # Act
        result = self.health_calc.bmi_full_classification(bmi)

        # Assert
        assert result == "Mild Thinness"

    @pytest.mark.parametrize("bmi", [18.5, 18.6, 22.0, 24.9, 24.99], ids=lambda x: f"BMI {x} -> Normal")
    def test_bmi_full_normal(self, bmi: float):
        """FULL BMI classification for Normal (18.5 <= bmi < 25.0)."""
        # Act
        result = self.health_calc.bmi_full_classification(bmi)

        # Assert
        assert result == "Normal"

    @pytest.mark.parametrize("bmi", [25.0, 25.1, 27.5, 29.9, 29.99], ids=lambda x: f"BMI {x} -> Overweight")
    def test_bmi_full_overweight(self, bmi: float):
        """FULL BMI classification for Overweight (25.0 <= bmi < 30.0)."""
        # Act
        result = self.health_calc.bmi_full_classification(bmi)

        # Assert
        assert result == "Overweight"

    @pytest.mark.parametrize("bmi", [30.0, 30.1, 34.9, 34.99], ids=lambda x: f"BMI {x} -> Obesity Class I")
    def test_bmi_full_obesity_class_i(self, bmi: float):
        """FULL BMI classification for Obesity Class I (30.0 <= bmi < 35.0)."""
        # Act
        result = self.health_calc.bmi_full_classification(bmi)

        # Assert
        assert result == "Obesity Class I"

    @pytest.mark.parametrize("bmi", [35.0, 35.1, 39.9, 39.99], ids=lambda x: f"BMI {x} -> Obesity Class II")
    def test_bmi_full_obesity_class_ii(self, bmi: float):
        """FULL BMI classification for Obesity Class II (35.0 <= bmi < 40.0)."""
        # Act
        result = self.health_calc.bmi_full_classification(bmi)

        # Assert
        assert result == "Obesity Class II"

    @pytest.mark.parametrize("bmi", [40.0, 40.1, 50.0, 75.0, 149.9, 150.0], ids=lambda x: f"BMI {x} -> Obesity Class III")
    def test_bmi_full_obesity_class_iii(self, bmi: float):
        """FULL BMI classification for Obesity Class III (bmi >= 40.0)."""
        # Act
        result = self.health_calc.bmi_full_classification(bmi)

        # Assert
        assert result == "Obesity Class III"

    #Tests for invalid BMI inputs (FULL classification)

    @pytest.mark.parametrize("bmi", [-50.0, -1.0, -0.01, 0.0], ids=lambda x: f"Invalid BMI (<=0): {x}")
    def test_bmi_full_invalid_minimum_raises(self, bmi: float):
        """Raise exception when BMI is zero or negative."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_full_classification(bmi)

    @pytest.mark.parametrize("bmi", [150.1, 200.0, 500.0], ids=lambda x: f"Invalid BMI (>150): {x}")
    def test_bmi_full_invalid_maximum_raises(self, bmi: float):
        """Raise exception when BMI is unrealistically high."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_full_classification(bmi)

    @pytest.mark.parametrize(
        "bmi",
        [math.nan, math.inf, -math.inf],
        ids=["BMI is NaN", "BMI is +inf", "BMI is -inf"],
    )
    def test_bmi_full_invalid_non_finite_raises(self, bmi: float):
        """Raise exception when BMI is not a finite real number."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_full_classification(bmi)