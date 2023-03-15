from salary_calc_fastapi.models.salary import Salary
from salary_calc_fastapi.tests.utils.test_classes import TestCaseWithDate


class TestSalaryModel(TestCaseWithDate):

    def test_no_deductions(self):
        salary = Salary(reference_salary=5000, date=self.date)
        self.assertEqual(5000, salary.net_salary)

    def test_basic_rate(self):
        salary = Salary(reference_salary=25000, date=self.date)
        self.assertEqual(21022.40, salary.net_salary)

    def test_higher_rate(self):
        salary = Salary(reference_salary=75000, date=self.date)
        self.assertEqual(52549.40, salary.net_salary)

    def test_additional_rate(self):
        salary = Salary(reference_salary=200000, date=self.date)
        self.assertEqual(117521.40, salary.net_salary)
