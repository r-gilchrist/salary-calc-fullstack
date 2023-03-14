from pydantic import BaseModel, validator
from salary_calc_fastapi.helpers.marginal_helpers import calculate_marginal_tax
from salary_calc_fastapi.models.date import Date
from salary_calc_fastapi.data import get_rate, get_threshold


class StudentLoan(BaseModel):
    gross_salary: float
    date: Date
    loan_type: str = "plan_1"

    def get_amount(self):
        if self.loan_type == "no_loan":
            return 0
        rate = get_rate("student_loan", self.loan_type, self.date)
        threshold = get_threshold("student_loan", self.loan_type, self.date)
        initial_calc = calculate_marginal_tax(self.gross_salary, rate, threshold)
        return int(initial_calc / 12) * 12

    @validator("gross_salary")
    def check_values_are_positive_numbers(cls, value):
        assert isinstance(value, float), "must be numeric"
        assert value >= 0, "cannot be negative"
        return value
