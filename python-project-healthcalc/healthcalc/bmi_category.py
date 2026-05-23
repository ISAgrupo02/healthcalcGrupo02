from enum import Enum


class BMICategory(Enum):
    SEVERE_THINNESS = "Severe Thinness"
    MODERATE_THINNESS = "Moderate Thinness"
    MILD_THINNESS = "Mild Thinness"
    NORMAL = "Normal"
    OVERWEIGHT = "Overweight"
    OBESE_CLASS_I = "Obesity Class I"
    OBESE_CLASS_II = "Obesity Class II"
    OBESE_CLASS_III = "Obesity Class III"
    