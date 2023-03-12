from pydantic import BaseModel
from salary_calc_fastapi.models.income_tax import IncomeTax
from salary_calc_fastapi.models.national_insurance import NationalInsurance
from salary_calc_fastapi.models.pension import Pension


class Salary(BaseModel):
    reference_salary: float
    percentage_employer: float | None = 0
    percentage_employee: float | None = 0

    def get_net(self):
        pension = Pension(reference_salary=self.reference_salary,
                          percentage_employee=self.percentage_employee,
                          percentage_employer=self.percentage_employer)

        gross_salary = self.reference_salary - pension.get_amount()

        income_tax = IncomeTax(gross_salary=gross_salary).get_amount()
        national_insurance = NationalInsurance(gross_salary=gross_salary).get_amount()

        return gross_salary - income_tax - national_insurance
