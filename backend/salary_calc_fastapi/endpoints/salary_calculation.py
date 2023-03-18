from fastapi_restful import Resource
from salary_calc_fastapi.models.salary import Salary
from salary_calc_fastapi.models.salary_request import SalaryRequest
from salary_calc_fastapi.models.salary_response import SalaryResponse


class SalaryCalculation(Resource):

    def post(self, salary_request: SalaryRequest) -> SalaryResponse:
        salary = Salary(
            reference_salary=salary_request.reference_salary,
            percentage_employee=salary_request.pension_contribution,
            loan_type=salary_request.student_loan_type,
            date=salary_request.date

        )
        return SalaryResponse(
            reference_salary=salary.reference_salary,
            income_tax=salary.income_tax,
            national_insurance=salary.national_insurance,
            student_loan=salary.student_loan,
            pension=salary.pension,
            net_salary=salary.net_salary,
        )
