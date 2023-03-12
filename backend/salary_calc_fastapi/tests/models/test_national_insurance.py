from unittest import TestCase
from pydantic import ValidationError
from salary_calc_fastapi.models.national_insurance import NationalInsurance


class TestIncomeTaxModel(TestCase):

    def test_no_tax(self):
        income_tax = NationalInsurance(gross_salary=5000)
        self.assertEqual(0, income_tax.get_amount())

    def test_basic_rate_taxpayer(self):
        income_tax = NationalInsurance(gross_salary=25000)
        self.assertEqual(1491.60, income_tax.get_amount())

    def test_higher_rate_taxpayer(self):
        income_tax = NationalInsurance(gross_salary=75000)
        self.assertEqual(5018.60, income_tax.get_amount())

    def test_gross_salary_must_be_positive(self):
        with self.assertRaises(ValidationError):
            NationalInsurance(gross_salary=-1000)
