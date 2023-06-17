from unittest import TestCase
from pydantic import ValidationError

from salary_calc_fastapi.models.pension import Pension


class TestPensionModel(TestCase):
    def test_correct_amount_is_returned(self):
        pension = Pension(
            reference_salary=100000, percentage_employee=5, percentage_employer=3
        )

        self.assertAlmostEqual(8000, pension())

    def test_correct_amount_is_returned_when_employer_contribution_is_zero(self):
        pension = Pension(
            reference_salary=25000, percentage_employee=10, percentage_employer=0
        )

        self.assertAlmostEqual(2500, pension())

    def test_correct_amount_is_returned_when_employee_contribution_is_zero(self):
        pension = Pension(
            reference_salary=50000, percentage_employee=0, percentage_employer=20
        )

        self.assertAlmostEqual(10000, pension())

    def test_default_pension_amount_is_zero(self):
        self.assertEqual(0, Pension(reference_salary=25000)())

    def test_negative_contributions_are_not_allowed_from_employer(self):
        with self.assertRaises(ValidationError):
            Pension(
                reference_salary=50000, percentage_employee=-3, percentage_employer=5
            )

    def test_negative_contributions_are_not_allowed_from_employee(self):
        with self.assertRaises(ValidationError):
            Pension(
                reference_salary=50000, percentage_employer=-5, percentage_employee=7
            )

    def test_inputs_must_be_numbers(self):
        with self.assertRaises(ValidationError):
            Pension(
                reference_salary=50000,
                percentage_employee="one",
                percentage_employer="two",
            )
