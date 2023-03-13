from fastapi_restful import Resource
from fastapi import Request
from salary_calc_fastapi.models.salary import Salary
from pydantic import BaseModel


class SalaryRequest(BaseModel):
    reference_salary: float
    pension_contribution: float


class SalaryCalculation(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self, example: SalaryRequest):
        salary = Salary(reference_salary=example.reference_salary, percentage_employee=example.pension_contribution)
        return {
            "reference_salary": example.reference_salary,
            "net_salary": salary.get_net(),
        }
