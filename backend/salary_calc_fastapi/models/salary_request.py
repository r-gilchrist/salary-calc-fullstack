from pydantic import BaseModel


class SalaryRequest(BaseModel):
    reference_salary: float
    pension_contribution: float
    student_loan_type: str
