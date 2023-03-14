from pydantic import BaseModel
from salary_calc_fastapi.models.income_tax import IncomeTax
from salary_calc_fastapi.models.national_insurance import NationalInsurance
from salary_calc_fastapi.models.student_loan import StudentLoan
from salary_calc_fastapi.models.pension import Pension
from salary_calc_fastapi.models.date import Date


class Salary(BaseModel):
    reference_salary: float
    date: Date
    percentage_employer: float | None = 0
    percentage_employee: float | None = 0
    loan_type: str = ""

    @property
    def pension(self):
        return Pension(
            reference_salary=self.reference_salary,
            percentage_employee=self.percentage_employee,
            percentage_employer=self.percentage_employer,
        ).get_amount()

    @property
    def gross_salary(self):
        return self.reference_salary - self.pension

    @property
    def income_tax(self):
        return IncomeTax(
            gross_salary=self.gross_salary,
            date=self.date
        ).get_amount()

    @property
    def national_insurance(self):
        return NationalInsurance(
            gross_salary=self.gross_salary,
            date=self.date
        ).get_amount()

    @property
    def student_loan(self):
        return StudentLoan(
            gross_salary=self.gross_salary,
            loan_type=self.loan_type
        ).get_amount()

    @property
    def net_salary(self):
        return self.gross_salary - self.income_tax - self.national_insurance - self.student_loan
