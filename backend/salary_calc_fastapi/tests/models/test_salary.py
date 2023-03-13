from unittest import TestCase
from salary_calc_fastapi.models.salary import Salary


class TestSalaryModel(TestCase):

    def test_no_deductions(self):
        salary = Salary(reference_salary=5000)
        self.assertEqual(5000, salary.net_salary)

    def test_basic_rate(self):
        salary = Salary(reference_salary=25000)
        self.assertEqual(21022.40, salary.net_salary)

    def test_higher_rate(self):
        salary = Salary(reference_salary=75000)
        self.assertEqual(52549.40, salary.net_salary)
