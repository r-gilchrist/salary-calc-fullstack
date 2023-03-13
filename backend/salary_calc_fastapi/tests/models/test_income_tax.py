from unittest import TestCase
from pydantic import ValidationError
from salary_calc_fastapi.models.income_tax import IncomeTax


class TestIncomeTaxModel(TestCase):

    def test_no_tax(self):
        income_tax = IncomeTax(gross_salary=5000)
        self.assertAlmostEqual(0, income_tax.get_amount())

    def test_basic_rate_taxpayer(self):
        income_tax = IncomeTax(gross_salary=25000)
        self.assertAlmostEqual(2486, income_tax.get_amount())

    def test_higher_rate_taxpayer(self):
        income_tax = IncomeTax(gross_salary=75000)
        self.assertAlmostEqual(17432, income_tax.get_amount())

    def test_gross_salary_must_be_positive(self):
        with self.assertRaises(ValidationError):
            IncomeTax(gross_salary=-1000)
