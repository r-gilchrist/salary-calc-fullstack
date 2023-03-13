from pydantic import BaseModel, validator
from salary_calc_fastapi.helpers.marginal_helpers import calculate_marginal_tax


class IncomeTax(BaseModel):
    gross_salary: float

    def _get_basic_contribution(self):
        return calculate_marginal_tax(self.gross_salary, 20, 12570, 50270)

    def _get_higher_contribution(self):
        return calculate_marginal_tax(self.gross_salary, 40, 50270)

    def get_amount(self):
        return self._get_basic_contribution() + \
               self._get_higher_contribution()

    @validator("gross_salary")
    def check_values_are_positive_numbers(cls, value):
        assert isinstance(value, float), "must be numeric"
        assert value >= 0, "cannot be negative"
        return value
