from pydantic import BaseModel, validator
from salary_calc_fastapi.helpers.marginal_helpers import calculate_marginal_tax


class StudentLoan(BaseModel):
    gross_salary: float
    loan_type: str = "plan_1"

    def get_amount(self):
        if self.loan_type == "plan_1":
            initial_calc = calculate_marginal_tax(self.gross_salary, 9, 20195)
        elif self.loan_type == "plan_2":
            initial_calc = calculate_marginal_tax(self.gross_salary, 9, 27295)
        else:
            return 0
        return int(initial_calc / 12) * 12

    @validator("gross_salary")
    def check_values_are_positive_numbers(cls, value):
        assert isinstance(value, float), "must be numeric"
        assert value >= 0, "cannot be negative"
        return value
