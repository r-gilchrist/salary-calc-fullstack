from unittest import TestCase
from pydantic import ValidationError

from salary_calc_fastapi.models.pension import Pension


class TestPensionModel(TestCase):

    def test_correct_amount_is_returned(self):
        pension = Pension(percentage_employee=5, percentage_employer=3)
        self.assertEqual(8000, pension.get_amount(reference_salary=100000))

    def test_correct_amount_is_returned_when_employer_contribution_is_zero(self):
        pension = Pension(percentage_employee=10, percentage_employer=0)
        self.assertEqual(2500, pension.get_amount(reference_salary=25000))

    def test_correct_amount_is_returned_when_employee_contribution_is_zero(self):
        pension = Pension(percentage_employee=0, percentage_employer=20)
        self.assertEqual(10000, pension.get_amount(reference_salary=50000))

    def test_default_pension_amount_is_zero(self):
        self.assertEqual(0, Pension().get_amount(reference_salary=25000))

    # def test_negative_contributions_are_not_allowed_from_employer(self):
    #     with self.assertRaises(ValidationError):
    #         Pension(percentage_employee=-3, percentage_employer=5)

    # def test_negative_contributions_are_not_allowed_from_employee(self):
    #     with self.assertRaises(ValidationError):
    #         Pension(percentage_employer=-5, percentage_employee=7)

    def test_inputs_must_be_numbers(self):
        with self.assertRaises(ValidationError):
            Pension(percentage_employee="one", percentage_employer="two")
