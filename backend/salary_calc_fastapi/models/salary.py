from pydantic import BaseModel
from salary_calc_fastapi.models.income_tax import IncomeTax
from salary_calc_fastapi.models.national_insurance import NationalInsurance
from salary_calc_fastapi.models.pension import Pension


class Salary(BaseModel):
    reference_salary: float
    percentage_employer: float | None = 0
    percentage_employee: float | None = 0

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
        return IncomeTax(gross_salary=self.gross_salary).get_amount()

    @property
    def national_insurance(self):
        return NationalInsurance(gross_salary=self.gross_salary).get_amount()

    @property
    def net_salary(self):
        return self.gross_salary - self.income_tax - self.national_insurance
