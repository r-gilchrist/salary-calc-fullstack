from fastapi_restful import Resource
from salary_calc_fastapi.models.salary import Salary
from pydantic import BaseModel


class SalaryRequest(BaseModel):
    reference_salary: float
    pension_contribution: float


class SalaryResponse(BaseModel):
    reference_salary: float
    income_tax: float
    national_insurance: float
    pension: float
    net_salary: float


class SalaryCalculation(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self, example: SalaryRequest) -> SalaryResponse:
        salary = Salary(reference_salary=example.reference_salary, percentage_employee=example.pension_contribution)
        return SalaryResponse(
            reference_salary=salary.reference_salary,
            income_tax=salary.income_tax,
            national_insurance=salary.national_insurance,
            pension=salary.pension,
            net_salary=salary.net_salary
        )
