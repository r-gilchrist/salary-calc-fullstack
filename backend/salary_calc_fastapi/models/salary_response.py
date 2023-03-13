from pydantic import BaseModel


class SalaryResponse(BaseModel):
    reference_salary: float
    income_tax: float
    national_insurance: float
    student_loan: float
    pension: float
    net_salary: float
