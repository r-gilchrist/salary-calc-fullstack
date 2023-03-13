from fastapi_restful import Resource
from salary_calc_fastapi.models.salary import Salary
from salary_calc_fastapi.models.salary_request import SalaryRequest
from salary_calc_fastapi.models.salary_response import SalaryResponse


class SalaryCalculation(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self, example: SalaryRequest) -> SalaryResponse:
        salary = Salary(
            reference_salary=example.reference_salary,
            percentage_employee=example.pension_contribution,
            loan_type=example.student_loan_type,
        )
        return SalaryResponse(
            reference_salary=salary.reference_salary,
            income_tax=salary.income_tax,
            national_insurance=salary.national_insurance,
            student_loan=salary.student_loan,
            pension=salary.pension,
            net_salary=salary.net_salary,
        )
