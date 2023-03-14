from pydantic import BaseModel
from salary_calc_fastapi.models.date import Date


class SalaryRequest(BaseModel):
    reference_salary: float
    pension_contribution: float
    student_loan_type: str
    date: Date
