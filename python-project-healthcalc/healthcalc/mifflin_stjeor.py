from healthcalc.otra_metrica import OtraMetrica
from healthcalc.person import Person
from healthcalc.gender import Gender
from healthcalc.exceptions import InvalidHealthDataException


class MifflinStJeor(OtraMetrica):

    def m(self, person: Person) -> float:

        weight = person.weight()
        height = person.height()
        age = person.age()
        gender = person.gender()

        if weight <= 0:
            raise InvalidHealthDataException(
                "Weight must be positive."
            )

        if height <= 0:
            raise InvalidHealthDataException(
                "Height must be positive."
            )

        if age <= 0:
            raise InvalidHealthDataException(
                "Age must be positive."
            )

        if gender == Gender.MALE:
            return (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                + 5
            )

        if gender == Gender.FEMALE:
            return (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                - 161
            )

        raise InvalidHealthDataException(
            "Invalid gender."
        )