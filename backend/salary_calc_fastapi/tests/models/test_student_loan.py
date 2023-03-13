from unittest import TestCase
from pydantic import ValidationError
from salary_calc_fastapi.models.student_loan import StudentLoan


class TestStudentLoanModel(TestCase):

    def test_plan_1(self):
        student_loan = StudentLoan(gross_salary=30000, loan_type="plan_1")
        self.assertAlmostEqual(876, student_loan.get_amount())

    def test_plan_2(self):
        student_loan = StudentLoan(gross_salary=30000, loan_type="plan_2")
        self.assertAlmostEqual(240, student_loan.get_amount())

    def test_gross_salary_must_be_positive(self):
        with self.assertRaises(ValidationError):
            StudentLoan(gross_salary=-1000)
